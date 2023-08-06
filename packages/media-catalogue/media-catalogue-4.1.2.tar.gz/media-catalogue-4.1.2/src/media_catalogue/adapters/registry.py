# -*- coding: utf-8 -*-

import sys

from django.db.models.signals import post_save, pre_delete
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from django.conf import settings
from django.db import DEFAULT_DB_ALIAS

from wagtail import hooks

__all__ = ['adapter_registry']


def is_running_without_database():
    engine = settings.DATABASES[DEFAULT_DB_ALIAS]['ENGINE']
    return engine == 'django.db.backends.dummy'


class AdapterRegistry(object):

    def __init__(self):
        self.adapters_by_label = dict()  # {app_name: {model_name: adapter}}
        self.adapters_by_content_type = dict()
        self.has_scanned_for_adapters = False
        self.handlers = dict()  # {'signal': {handler: None}}
        self._signals = [post_save, pre_delete]

    def _scan_for_media_catalogue_adapters(self):

        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return

        if not self.has_scanned_for_adapters:

            for adapter in hooks.get_hooks('register_media_catalogue_adapter'):
                self._register_adapter(adapter)

            self.has_scanned_for_adapters = True

    def _register_adapter(self, adapter):

        global LAST_FAKE_CONTENT_TYPE_ID

        from .adapter import MediaCatalogueAdapter

        if not isinstance(adapter, MediaCatalogueAdapter):
            raise Exception("{} is not an instance of {}".format(
                    adapter.__class__.__name__, MediaCatalogueAdapter.__name__))

        model_app_label = adapter.model._meta.app_label
        model_name = adapter.model._meta.model_name

        adapters_for_app = self.adapters_by_label.setdefault(model_app_label, {})
        adapters_for_app.setdefault(model_name, adapter)

        content_type = ContentType.objects.get_for_model(adapter.model)
        adapter_for_content_type_id = self.adapters_by_content_type.setdefault(content_type.id, [])

        if adapter_for_content_type_id:
            raise RuntimeError("Content type with id {:d} already has media catalogue adapter.".format(content_type.id))

        adapter_for_content_type_id.append(adapter)

        for signal in self._signals:
            # weak=False: Otherwise the decorated lambda will be garbage collected!
            decorator = receiver(signal, sender=adapter.model, weak=False)
            decorator(lambda **kwargs: self._handle_signal(**kwargs))

    def _handle_signal(self, signal, **kwargs):

        handler_entries = self.handlers.get(signal, {})

        for handler in handler_entries.keys():
            handler(**kwargs)

    @property
    def adapters(self):
        self._scan_for_media_catalogue_adapters()
        return [value[0] for value in self.adapters_by_content_type.values()]

    @property
    def adapter_content_types(self):
        self._scan_for_media_catalogue_adapters()
        return list(self.adapters_by_content_type.keys())

    def get_adapter_for_app_model(self, app_label, model_name=None):

        self._scan_for_media_catalogue_adapters()

        if model_name is None:
            app_label, model_name = app_label.split(".")

        return self.adapters_by_label.get(app_label, {}).get(model_name, None)

    def get_adapter_for_content_type_id(self, content_type_id):

        self._scan_for_media_catalogue_adapters()

        return self.adapters_by_content_type.get(content_type_id, [None])[0]

    def register_signal_handler(self, signal, handler):
        handlers = self.handlers.setdefault(signal, {})
        handlers.setdefault(handler, None)

    def deregister_signal_handler(self, signal, handler):
        handlers = self.handlers.setdefault(signal, {})
        handlers.setdefault(handler, None)


adapter_registry = AdapterRegistry()
