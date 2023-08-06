# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from types import SimpleNamespace

import os


from django.db.models import Count
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import path, re_path
from django.utils.text import capfirst
from django.utils.deconstruct import deconstructible
from taggit.models import Tag

from wagtail.admin.templatetags.wagtailadmin_tags import ellipsistrim

from wagtail_content_admin.content_admin import ContentAdmin
from wagtail_content_admin.frontend import ContentItemAction

from aldine import ResponsiveDelegate

from ..models.universal_media_items import UniversalMediaItem
from ..apps import get_app_label
from .registry import adapter_registry

__all__ = ['MediaCatalogueAdapter', 'standard_adapter', 'universal_adapter',
           'get_media_catalogue_adapter', 'generalize']

APP_LABEL = get_app_label()


@deconstructible
class MediaCatalogueAdapter(ResponsiveDelegate, ContentAdmin):

    do_not_call_in_templates = True

    browser_order_by = ['-created_at']
    browser_add_url_name = 'add'
    browser_edit_url_name = 'edit'
    browser_delete_url_name = 'delete'
    browser_delete_multiple_url_name = 'delete_multiple'

    server_url_name = 'serve'

    editor_permissions = ['change']
    deletion_permissions = ['delete']

    @property
    def add_url_specifiers(self):
        return self.add_url_specifiers_

    @property
    def server_url_specifier(self):
        return self.url_namespace + ':' + self.server_url_name

    def __init__(self, model, permission_policy, add_url_specifiers=None):

        self.model = model # To make sure that get_verbose_name() works in super().__init__()

        super().__init__()

        if add_url_specifiers is None:
            add_url_specifiers = []

        self.url_namespace = APP_LABEL

        self.browser_add_url_specifier = APP_LABEL + ':' + self.browser_add_url_name
        self.browser_edit_url_specifier = APP_LABEL + ':' + self.browser_edit_url_name
        self.browser_delete_url_specifier = APP_LABEL + ':' + self.browser_delete_url_name
        self.browser_delete_multiple_url_specifier = APP_LABEL + ':' + self.browser_delete_multiple_url_name

        if settings.MEDIA_CATALOGUE_UNIFY_MEDIA:

            def key_for_instance(instance):

                if instance is None:
                    return None

                universal_media_item = UniversalMediaItem.objects.get(content_id=instance.pk, content_type=instance.content_type.id)

                if universal_media_item is None:
                    return None

                return universal_media_item.pk

            self.browser_get_key_for_instance = key_for_instance

        self.permission_policy = permission_policy
        self.add_url_specifiers_ = list(add_url_specifiers)

        self.default_actions = [
            ContentItemAction('move_forward', title='Move Forward', icon='arrow-up'),
            ContentItemAction('move_backward', title='Move Backward', icon='arrow-down'),
            ContentItemAction('delete', title='Delete', icon='bin')]

        self.browser_bulk_action_app_label = model._meta.app_label
        self.browser_bulk_action_model_name = model._meta.model_name
        self.browser_bulk_action_type = 'MEDIA ITEM'

    def create_browser_admin_views(self):

        views = super(MediaCatalogueAdapter, self).create_browser_admin_views()

        from ..views.add import media_type_selection

        views.media_type_selection = media_type_selection

        from ..views.editor import Editor

        arguments = {
            'adapter': self,
            'permissions': self.editor_permissions
        }

        views.editor = Editor.as_view(**arguments)

        from ..views.deletion import Deletion

        arguments = {
            'adapter': self,
            'permissions': self.deletion_permissions
        }

        views.deletion = Deletion.as_view(**arguments)

        return views

    def create_browser_admin_urls(self):

        views = self.create_browser_admin_views()
        urlpatterns = super(MediaCatalogueAdapter, self).create_browser_admin_urls()

        urlpatterns += [
            path('add/', views.media_type_selection, name=self.browser_add_url_name),
            path('delete/multiple/', views.deletion, name=self.browser_delete_multiple_url_name),
            path('delete/<str:media_item_pk>/', views.deletion, name=self.browser_delete_url_name),
            # path('edit/multiple/<str:media_item_pk>/', edit_multiple.EditView.as_view(), name='edit_multiple'),
            path('edit/<str:media_item_pk>/', views.editor, name=self.browser_edit_url_name),
        ]

        return urlpatterns

    def create_server_views(self):

        from ..views.server import Server

        arguments = {
            'adapter': self,
            'permissions': self.chooser_permissions
        }

        result = SimpleNamespace()
        result.server_view = Server.as_view(**arguments)
        return result

    def create_server_urls(self):

        views = self.create_server_views()

        urlpatterns = [
            re_path(r'^(\d+)/([^/]+)/([^/]*/)?$', views.server_view, name=self.server_url_name)
        ]

        return urlpatterns

    def create_views(self):

        views = super(MediaCatalogueAdapter, self).create_views() + self.create_server_views()
        return views

    def create_urls(self):

        urlpatterns = super(MediaCatalogueAdapter, self).create_urls() + self.create_server_urls()
        return urlpatterns

    def get_popular_tags(self, count=10):
        content_type = ContentType.objects.get_for_model(self.model)

        return Tag.objects.filter(
            taggit_taggeditem_items__content_type=content_type
        ).annotate(
            item_count=Count('taggit_taggeditem_items')
        ).order_by('-item_count')[:count]

    def get_verbose_name(self, instance=None, plural=False):
        if instance is not None:
            return capfirst(
                instance.specific_class._meta.verbose_name if not plural else self.model._meta.verbose_name_plural)  # noqa

        return capfirst(self.model._meta.verbose_name if not plural else self.model._meta.verbose_name_plural) # noqa

    # noinspection PyMethodMayBeStatic
    def title_for(self, instance):
        return instance.specific.title

    # noinspection PyMethodMayBeStatic
    def content_url_for(self, instance, file_name):
        return None  # return instance.specific.content_url_for(file_name)

    # noinspection PyMethodMayBeStatic
    def content_path_for(self, instance, file_name):
        return os.path.join(instance.specific.content_path, file_name)

    def user_can_edit_model(self, user):
        return self.permission_policy.user_has_permission(user, 'edit')

    # noinspection PyMethodMayBeStatic
    def create_panel_for(self, instance, request):

        instance = instance.specific

        # noinspection PyPep8Naming
        instance_class = instance.__class__

        # Make edit handler
        panel = instance_class.edit_handler
        panel = panel.bind_to_model(model=instance_class)

        return panel

    # noinspection PyMethodMayBeStatic
    def delete_instance(self, instance):
        instance.specific.delete()

    # noinspection PyMethodMayBeStatic
    def bulk_delete_instances(self, instances):

        for instance in instances:
            instance.specific.delete()

    def render_in_responsive_cell(self, item, cell, template_context=None):

        if not item:
            return ''

        return item.render_in_responsive_cell(cell, template_context=template_context)

    def render_preview_inner(self, instance, **kwargs):

        preview_html = ''

        if hasattr(instance.specific, 'render_preview_html'):
            preview_html = instance.specific.render_preview_html()

        return '<div class="fit-content">{}</div>'.format(preview_html)

    def render_preview(self, instance, **kwargs):
        inner = self.render_preview_inner(instance, **kwargs)
        title = ellipsistrim(self.title_for(instance), 60)
        return '<figure class="content-item-preview"><span class="content-item-category-label">{}</span>{}<figcaption>{}</figcaption></figure>'.format(
            self.get_verbose_name(instance=instance),
            inner,
            ellipsistrim(title, 60))

    def render_entry_inner(self, instance, **kwargs):
        preview_html = self.render_preview(instance, **kwargs)
        return preview_html

        #edit_url = self.edit_url_for(instance)
        #return '<a href="{}">{}</a>'.format(
        #    edit_url,
        #    preview_html)

    def render_choice_inner(self, instance, annotations_id="", **kwargs):
        preview_html = self.render_preview(instance, **kwargs)
        return '<a href="{}">{}</a>'.format(
            self.content_item_chosen_url_for(instance, annotations_id),
            preview_html)

    def render_choice(self, instance, **kwargs):
        inner = self.render_choice_inner(instance, **kwargs)
        return '<div class="content-item-choice">{}</div>'.format(inner)

    def configure_frontend_item(self, frontend_item, instance):
        frontend_item.model_verbose_name = self.get_verbose_name(instance=instance)
        frontend_item.title = self.title_for(instance)
        frontend_item.preview_html = self.render_preview(instance)

        edit = ContentItemAction('edit', title='Edit', url=self.edit_url_for(instance))
        frontend_item.add_action(edit)


class RegistryCatalogueAdapter(MediaCatalogueAdapter):

    @property
    def add_url_specifiers(self):

        if not self.add_url_specifiers_:

            self.add_url_specifiers_ = []

            for adapter in adapter_registry.adapters:
                self.add_url_specifiers_.extend(adapter.add_url_specifiers)

        return self.add_url_specifiers_

    def __init__(self, model, permission_policy):

        super().__init__(model=model,
                         permission_policy=permission_policy,
                         add_url_specifiers=[])

    def get_popular_tags(self, count=10):
        content_types = adapter_registry.adapter_content_types

        return Tag.objects.filter(
            taggit_taggeditem_items__content_type__in=content_types
        ).annotate(
            item_count=Count('taggit_taggeditem_items')
        ).order_by('-item_count')[:count]


class StandardCatalogueAdapter(RegistryCatalogueAdapter):

    def __init__(self):

        from ..models.permissions import permission_policy as media_item_permission_policy
        from ..models import MediaItem

        super().__init__(model=MediaItem,
                         permission_policy=media_item_permission_policy)


class UniversalCatalogueAdapter(RegistryCatalogueAdapter):

    def __init__(self):

        from ..models import MediaItem, UniversalMediaItem, permission_policy as universal_item_permission_policy

        self.verbose_name_ = MediaItem._meta.verbose_name
        self.verbose_name_plural_ = MediaItem._meta.verbose_name_plural

        super().__init__(model=UniversalMediaItem,
                         permission_policy=universal_item_permission_policy)

    def get_popular_tags(self, count=10):
        content_types = adapter_registry.adapter_content_types

        return Tag.objects.filter(
            taggit_taggeditem_items__content_type__in=content_types
        ).annotate(
            item_count=Count('taggit_taggeditem_items')
        ).order_by('-item_count')[:count]

    # noinspection PyMethodMayBeStatic
    def edit_url_for(self, instance):
        return instance.adapter.edit_url_for(instance.specific)

    # noinspection PyMethodMayBeStatic
    def delete_url_for(self, instance):
        return instance.adapter.delete_url_for(instance.specific)

    def render_preview_inner(self, instance, **kwargs):
        return instance.adapter.render_preview_inner(instance.specific)

    # noinspection PyMethodMayBeStatic
    def title_for(self, instance):
        return instance.adapter.title_for(instance.specific)

    # noinspection PyMethodMayBeStatic
    def content_url_for(self, instance, file_name):
        return instance.adapter.content_url_for(instance.specific, file_name)

    # noinspection PyMethodMayBeStatic
    def content_path_for(self, instance, file_name):
        return instance.adapter.content_path_for(instance.specific, file_name)

    # noinspection PyMethodMayBeStatic
    def create_panel_for(self, instance, request):
        return instance.adapter.create_panel_for(instance.specific, request)

    # noinspection PyMethodMayBeStatic
    def delete_instance(self, instance):
        instance.adapter.delete_instance(instance.specific)
        instance.delete()

    # noinspection PyMethodMayBeStatic
    def bulk_delete_instances(self, instances):
        for instance in instances:
            instance.adapter.delete_instance(instance.specific)
            instance.delete()
            
    def render_in_responsive_cell(self, item, cell, template_context=None):

        if not item:
            return ''

        return item.adapter.render_in_responsive_cell(item.specific, cell, template_context=template_context)


standard_adapter = None
universal_adapter = None


def get_media_catalogue_adapter():

    global standard_adapter
    global universal_adapter

    if settings.MEDIA_CATALOGUE_UNIFY_MEDIA:

        if universal_adapter is None:
            universal_adapter = UniversalCatalogueAdapter()

        adapter = universal_adapter
    else:

        if standard_adapter is None:
            standard_adapter = StandardCatalogueAdapter()

        adapter = standard_adapter

    return adapter


def generalize(instance):

    if not settings.MEDIA_CATALOGUE_UNIFY_MEDIA:
        return instance

    content_type = ContentType.objects.get_for_model(instance)
    universal_type = ContentType.objects.get_for_model(UniversalMediaItem)

    if content_type is not universal_type:
        instance = UniversalMediaItem.objects.get(content_type=content_type, content_id=instance.pk)

    return instance
