# -*- coding: utf-8 -*-

from types import SimpleNamespace
import sys

from django.apps import AppConfig
from django.apps import apps
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.db import DEFAULT_DB_ALIAS
from django.core.exceptions import ImproperlyConfigured


def is_running_without_database():
    engine = settings.DATABASES[DEFAULT_DB_ALIAS]['ENGINE']
    return engine == 'django.db.backends.dummy'


class MediaCatalogueConfig(AppConfig):
    name = 'media_catalogue'
    label = 'media_catalogue'
    verbose_name = _("Media Catalogue")
    default_auto_field = 'django.db.models.BigAutoField'
    app_settings_getters = SimpleNamespace()

    def import_models(self):

        from django_auxiliaries.app_settings import configure

        self.app_settings_getters = configure(self)

        super().import_models()

    def ready(self):

        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return

        from .adapters.registry import adapter_registry
        _ = adapter_registry.adapters

        from .models import MediaItem
        MediaItem.register_storage_signal_handlers()

        from wagtail.admin.menu import admin_menu

        if settings.MEDIA_CATALOGUE_HIDE_IMAGES_IN_ADMIN_MENU and hasattr(admin_menu, 'registered_menu_items'):
            menu_indices = reversed([index for index, item in enumerate(admin_menu.registered_menu_items)
                                     if item.url.startswith('/admin/images/')])
            menu_items = admin_menu.registered_menu_items

            for index in menu_indices:
                del menu_items[index]


def get_app_label():
    return MediaCatalogueConfig.label


def reverse_app_url(identifier):
    return reverse(f'{MediaCatalogueConfig.label}:{identifier}')


def get_media_item_model_string():
    return getattr(settings, 'MEDIA_CATALOGUE_MEDIA_ITEM_MODEL', 'media_catalogue.MediaItem')


def get_media_item_model():
    from django.apps import apps
    model_string = get_media_item_model_string()
    try:
        return apps.get_model(model_string, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("MEDIA_CATALOGUE_MEDIA_ITEM_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "MEDIA_CATALOGUE_MEDIA_ITEM_MODEL refers to model '%s' that has not been installed" % model_string
        )


def get_app_config():
    return apps.get_app_config(MediaCatalogueConfig.label)
