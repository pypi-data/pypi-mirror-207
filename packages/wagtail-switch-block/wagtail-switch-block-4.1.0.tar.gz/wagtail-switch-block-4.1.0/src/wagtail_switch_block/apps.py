# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class WagtailSwitchBlockConfig(AppConfig):
    # noinspection SpellCheckingInspection
    name = 'wagtail_switch_block'
    # noinspection SpellCheckingInspection
    label = 'wagtail_switch_block'
    verbose_name = _("Wagtail Switch Block")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):

        from .blocks import update_dynamic_switch_blocks

        update_dynamic_switch_blocks()

        from .blocks import SwitchBlock, SwitchBlockAdapter
        from wagtail.telepath import register

        register(SwitchBlockAdapter(), SwitchBlock)


def get_app_label():
    return WagtailSwitchBlockConfig.label


def reverse_app_url(identifier):
    return reverse(f'{WagtailSwitchBlockConfig.label}:{identifier}')
