from collections import namedtuple
import inspect
import importlib

from django.apps import apps
from django.utils.encoding import force_str
from django.utils.text import capfirst

__all__ = ['BlockRegistry']


def get_caller_module(level=1):

    stack = inspect.stack()
    start = 0 + level

    if len(stack) < start + 1:
        return None

    parentframe = stack[start][0] # noqa

    module_info = inspect.getmodule(parentframe)

    if not module_info:
        return None

    module = importlib.import_module(module_info.__name__)

    # Remove reference to frame
    del parentframe

    return module


class BlockRegistry:

    Entry = namedtuple('Entry', ['block_type', 'block_args', 'block_kwargs', 'block_prototype', 'kwargs'])

    def __init__(self):
        self.__entries = {}

    def define_procedures_in_caller_module(self, name):

        module = get_caller_module(level=2)

        def register_block(*args, **kwargs):
            return self.register_block(*args, **kwargs)

        def block_choices(switch_block):
            return self.instantiate_blocks_for_switch_block(switch_block)

        setattr(module, "register_{}_block".format(name), register_block)
        setattr(module, "{}_block_choices".format(name), block_choices)

    # noinspection PyMethodMayBeStatic
    def should_register_block(self, app_label, local_identifier, block_type, block_args, block_kwargs, **kwargs):
        return True

    def register_block(self, app_label, local_identifier, block_type, block_args, block_kwargs, **kwargs):

        if not self.should_register_block(app_label, local_identifier, block_type, block_args, block_kwargs, **kwargs):
            return

        identifier = app_label + "_" + local_identifier

        if "label" not in block_kwargs:
            config = apps.get_app_config(app_label)
            label = capfirst(force_str(local_identifier).replace("_", " ")) + " [{}]".format(config.verbose_name)
            block_kwargs["label"] = label

        block = block_type(*block_args, **block_kwargs)

        self.__entries[identifier] = self.Entry(block_type=block_type, block_args=block_args, block_kwargs=block_kwargs,
                                                block_prototype=block, kwargs=kwargs)

        return identifier

    def instantiate_blocks_for_switch_block(self, switch_block):

        result = []

        for identifier, entry in self.__entries.items():

            if not self.should_include_entry_for_switch_block(identifier, entry, switch_block):
                continue

            block = self.instantiate_block(identifier, entry, switch_block)
            result.append((identifier, block))

        return result

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_switch_block(self, identifier, entry, switch_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, switch_block):
        block = entry.block_type(*entry.block_args, **entry.block_kwargs)
        block.set_name(identifier)

        return block

