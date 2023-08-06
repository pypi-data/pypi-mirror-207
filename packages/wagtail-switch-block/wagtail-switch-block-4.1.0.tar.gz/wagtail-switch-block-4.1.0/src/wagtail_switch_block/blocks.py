import importlib
import sys
import collections

from django import forms

from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from wagtail import blocks

from wagtail.blocks.struct_block import StructBlockAdapter, StructBlockValidationError

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static

from .apps import get_app_label
from .function_specifier import FunctionSpecifier


__all__ = ['SwitchBlock', 'SwitchValue', 'SwitchBlockAdapter', 'update_dynamic_switch_blocks', 'DynamicSwitchBlock',
           'register_dynamic_switch_block']

APP_LABEL = get_app_label()


TYPE_FIELD_NAME = '__type__'  # This is also used in the JavaScript client-side code for locating the element


class SwitchValue(blocks.StructValue):

    @property
    def type(self):
        return self[TYPE_FIELD_NAME]

    @property
    def value(self):
        return self[self[TYPE_FIELD_NAME]]

    @value.setter
    def value(self, value):
        self[self[TYPE_FIELD_NAME]] = value


class ProtoSwitchBlock(blocks.BaseStructBlock):

    TYPE_FIELD_NAME = TYPE_FIELD_NAME

    error_messages = {
        "missing_type_field": _("Please make a choice."),
        "invalid_type": _("Please make a choice."),
    }

    class Meta:
        template = APP_LABEL + "/switch_block.html"
        value_class = SwitchValue
        default_block_name = None
        default = {}
        form_classname = "struct-block switch-block"
        choice_label = "Type"

    def __init__(self, *, local_blocks=None, default_block_name=None, **kwargs):

        meta = self._meta_class()

        if not meta.default_block_name and not default_block_name:

            names = list(self.declared_blocks.keys()) # noqa

            if not names and local_blocks:
                names = [local_blocks[0][0]]
            else:
                names = [None]

            default_block_name = names[0]

        super().__init__(local_blocks=local_blocks, default_block_name=default_block_name, **kwargs)

        self.choice_block = None
        self.update_child_blocks()

    def create_choice_block(self, choices, default_choice):

        choice_block = blocks.ChoiceBlock(label=self.meta.choice_label, choices=choices, default=default_choice)
        choice_block.set_name(TYPE_FIELD_NAME)
        return choice_block

    def update_child_blocks(self):

        choices = [(name, block.label) for name, block in self.child_blocks.items()]

        if not choices:
            raise RuntimeError("At least one choice needs to be defined.")

        default_choice = choices[0][0] if choices else None

        if self.meta.default_block_name:
            default_choice = self.meta.default_block_name

        self.choice_block = self.create_choice_block(choices, default_choice)

        new_child_blocks = collections.OrderedDict(((self.choice_block.name, self.choice_block),))
        new_child_blocks.update(self.child_blocks)

        self.child_blocks = new_child_blocks

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    def extract_references(self, value):

        block = self.child_blocks[value.type]
        return block.extract_references(value.value)

    def _prune_value(self, value):

        choice = value.get(TYPE_FIELD_NAME, self.meta.default_block_name)

        for name in list(value.keys()):

            if name != choice and name != TYPE_FIELD_NAME:
                del value[name]

        return value

    def get_default(self):
        result = super().get_default()
        result = self._prune_value(result)
        return result

    def value_from_datadict(self, data, files, prefix):
        result = super(ProtoSwitchBlock, self).value_from_datadict(data, files, prefix)

        # ChoiceBlock returns None if the key is not in the dictionary, so supply default
        if result[TYPE_FIELD_NAME] is None:
            result[TYPE_FIELD_NAME] = self.meta.default_block_name

        return self._prune_value(result)

    def value_omitted_from_data(self, data, files, prefix):

        type_field_prefix = "%s-%s" % (prefix, TYPE_FIELD_NAME)
        choice_is_missing = self.child_blocks[TYPE_FIELD_NAME].value_omitted_from_data(data, files, type_field_prefix)

        if choice_is_missing:
            return True

        choice = self.child_blocks[TYPE_FIELD_NAME].value_from_datadict(data, files, type_field_prefix)

        if choice not in self.child_blocks:
            return True

        return self.child_blocks[choice].value_omitted_from_data(data, files, "%s-%s" % (prefix, choice))

    def clean(self, value):

        if TYPE_FIELD_NAME not in value:
            raise ValidationError(self.error_messages["missing_type_field"], code="missing_type_field")

        if value.type not in self.child_blocks:
            raise ValidationError(self.error_messages["invalid_type"], code="invalid_type")

        errors = {}

        try:
            clean_choice = self.child_blocks[value.type].clean(value.value)
        except ValidationError as e:
            errors[value.type] = ErrorList([e])
            raise StructBlockValidationError(errors)

        result = {
            TYPE_FIELD_NAME: value.type,
            value.type: clean_choice
        }

        return self._to_struct_value(result)

    def get_form_state(self, value):

        state = dict([
            (name, self.child_blocks[name].get_form_state
                (value[name] if name in value else self.child_blocks[name].get_default()))
            for name in self.child_blocks.keys()
        ])

        return state

    def get_form_context(self, value, prefix='', errors=None):
        context = super(ProtoSwitchBlock, self).get_form_context(value, prefix, errors)
        return context

    def to_python(self, value):

        result = super().to_python(value)
        result = self._prune_value(result)
        return result

    def bulk_to_python(self, values):

        values = super().bulk_to_python(values)
        values = [self._prune_value(value) for value in values]
        return values

    def get_prep_value(self, value):

        choice = value.get(TYPE_FIELD_NAME, self.meta.default_block_name)
        block = self.child_blocks[choice]

        return {
            TYPE_FIELD_NAME: self.choice_block.get_prep_value(choice),
            choice: block.get_prep_value(value.get(choice, block.get_default()))
        }

    def get_searchable_content(self, value):

        choice = value.get(TYPE_FIELD_NAME, self.meta.default_block_name)
        block = self.child_blocks[choice]

        content = [
            block.get_searchable_content(value.get(choice, block.get_default()))
        ]

        return content


mod = sys.modules[__name__]

try:
    model_porter = importlib.import_module("model_porter")

    from model_porter.support_mixin import ModelPorterSupportMixin

    class BaseSwitchBlock(ModelPorterSupportMixin, ProtoSwitchBlock):

        # noinspection PyMethodMayBeStatic
        def from_repository(self, value, context):

            for name in list(value.keys()):

                if name == TYPE_FIELD_NAME or name not in self.child_blocks:
                    continue

                child_block = self.child_blocks[name]

                if not isinstance(child_block, ModelPorterSupportMixin):
                    continue

                value[name] = child_block.from_repository(value[name], context)

            return value


except (ImportError, ModuleNotFoundError):
    model_porter = None
    BaseSwitchBlock = ProtoSwitchBlock


class SwitchBlock(BaseSwitchBlock, metaclass=blocks.DeclarativeSubBlocksMetaclass):
    pass


class SwitchBlockAdapter(StructBlockAdapter):

    # noinspection SpellCheckingInspection
    js_constructor = APP_LABEL + '.SwitchBlock'

    def js_args(self, block):
        result = super(SwitchBlockAdapter, self).js_args(block)
        return result

    @cached_property
    def media(self):
        # noinspection SpellCheckingInspection
        return forms.Media(css={'all': [
            tagged_static(APP_LABEL + '/css/wagtail_switch_block.css'),
        ]},
            js=[
                tagged_static("wagtailadmin/js/telepath/blocks.js"),
                tagged_static(APP_LABEL + '/js/wagtail_switch_block.js')
            ])


# register(SwitchBlockAdapter(), SwitchBlock)

REGISTRY = {}
blocks_in_registry_were_updated = False


def register_dynamic_switch_block(block):
    REGISTRY[id(block)] = block


def update_dynamic_switch_blocks():

    global blocks_in_registry_were_updated

    if blocks_in_registry_were_updated:
        return

    blocks_in_registry_were_updated = True

    traversed = set()

    while True:

        remaining = traversed.symmetric_difference(REGISTRY.keys())

        if not remaining:
            break

        for key in remaining:
            block = REGISTRY[key]
            block.update_child_blocks()

        traversed.update(remaining)


class DynamicSwitchBlock(SwitchBlock):

    def __init__(self, *, child_blocks_function_name, default_block_name=None, **kwargs):

        if "local_blocks" in kwargs:
            del kwargs["local_blocks"]

        self.child_blocks_function = FunctionSpecifier(function_path=child_blocks_function_name)

        super().__init__(default_block_name=default_block_name, **kwargs)

        register_dynamic_switch_block(self)

    def deconstruct(self):

        _, args, kwargs = super().deconstruct()
        path = APP_LABEL + '.DynamicSwitchBlock'
        return path, args, kwargs

    def update_child_blocks(self):

        child_blocks = self.child_blocks_function(switch_block=self)

        choices = [(name, block.label) for name, block in child_blocks]

        default_choice = choices[0][0] if choices else None

        if self.meta.default_block_name:
            default_choice = self.meta.default_block_name

        self.choice_block = self.create_choice_block(choices, default_choice)

        new_child_blocks = collections.OrderedDict(((self.choice_block.name, self.choice_block),))
        new_child_blocks.update(child_blocks)

        self.child_blocks = new_child_blocks
