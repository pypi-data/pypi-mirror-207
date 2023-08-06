# -*- coding: utf-8 -*-

from types import SimpleNamespace
from django.urls import reverse
from django.apps import AppConfig
from django.apps import apps
from django.utils.translation import gettext_lazy as _

from wagtail.utils.decorators import cached_classmethod

PAGE_EDIT_HANDLERS = set()


class WagtailSynopsisConfig(AppConfig):
    name = 'wagtail_synopsis'
    label = 'wagtail_synopsis'
    verbose_name = _("Wagtail Synopsis")
    default_auto_field = 'django.db.models.BigAutoField'
    app_settings_getters = SimpleNamespace()

    def import_models(self):

        from django_auxiliaries.app_settings import configure

        self.app_settings_getters = configure(self)

        super().import_models()

    def ready(self):

        from .models import PageSynopsis, sync_page_synopsis, determine_page_url
        from wagtail.models import Page

        page_adapter = PageSynopsis.install_synopsis_adapter_for(
            editable_fields=['summary', 'visual', 'tags'],
            sync_method=sync_page_synopsis,
            determine_url_method=determine_page_url)

        base_get_edit_handler = Page.get_edit_handler

        @cached_classmethod
        def get_page_edit_handler(cls):
            from wagtail.admin.panels import TabbedInterface

            # access the original function to derive the edit handler
            edit_handler = base_get_edit_handler.fn(cls) # noqa

            if isinstance(edit_handler, TabbedInterface) and id(edit_handler) not in PAGE_EDIT_HANDLERS:
                PAGE_EDIT_HANDLERS.add(id(edit_handler))
                synopsis_panel = page_adapter.create_synopsis_panel_for(cls)
                if synopsis_panel not in edit_handler.children:
                    edit_handler.children.insert(1, synopsis_panel)

            return edit_handler

        Page.get_edit_handler = get_page_edit_handler


def get_app_label():
    return WagtailSynopsisConfig.label


def reverse_app_url(identifier):
    return reverse(f'{WagtailSynopsisConfig.label}:{identifier}')


def get_app_config():
    return apps.get_app_config(WagtailSynopsisConfig.label)
