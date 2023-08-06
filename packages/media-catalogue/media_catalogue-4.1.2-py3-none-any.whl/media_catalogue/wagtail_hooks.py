from django.urls import include, path, reverse
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext
from django.utils.html import format_html

from wagtail.admin.menu import MenuItem
from wagtail import hooks

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static

from . import admin_urls
from .apps import get_app_label
from .models import MediaItem
from .models.permissions import permission_policy

from .views.bulk_actions import (
    AddTagsBulkAction, AddToCollectionBulkAction, DeleteBulkAction)

from .image_adapter import ImageAdapter

APP_LABEL = get_app_label()


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path(APP_LABEL + '/', include(admin_urls, namespace=APP_LABEL)),
    ]


class MediaMenuItem(MenuItem):
    def is_shown(self, request):
        return permission_policy.user_has_any_permission(
            request.user, ['add', 'change', 'delete']
        )


@hooks.register('register_admin_menu_item')
def register_media_catalogue_menu_item():
    return MediaMenuItem(
        _('Media Catalogue'), reverse(f'{APP_LABEL}:index'),
        name='media items', icon_name='image', order=300
    )


@hooks.register('describe_collection_contents')
def describe_collection_docs(collection):
    media_items_count = MediaItem.objects.filter(collection=collection).count()

    if not media_items_count:
        return

    url = reverse(f'{APP_LABEL}:index') + ('?collection_id=%d' % collection.id)

    return {
        'count': media_items_count,
        'count_text': ngettext(
            "%(count)s media item",
            "%(count)s media items",
            media_items_count
        ) % {'count': media_items_count},
        'url': url,
    }


# @hooks.register("insert_editor_js")
def editor_js():
    return format_html(
        """
        <script>
            window.chooserUrls.contentChooser = '{0}';
            window.chooserUrls.mediaItemChooser = '{0}';
        </script>
        """,
        reverse(APP_LABEL + ":chooser"),
    )


@hooks.register("insert_global_admin_css")
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        tagged_static(APP_LABEL + '/css/media_catalogue_admin.css')
    )


for action_class in [AddTagsBulkAction, AddToCollectionBulkAction, DeleteBulkAction]:
    hooks.register('register_bulk_action', action_class)

hooks.register('register_media_catalogue_adapter', ImageAdapter())
