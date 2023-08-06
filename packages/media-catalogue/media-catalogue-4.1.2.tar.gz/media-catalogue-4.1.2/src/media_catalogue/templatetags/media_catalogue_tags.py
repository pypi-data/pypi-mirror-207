
from django import template
from django.core.exceptions import ImproperlyConfigured
from django.urls import NoReverseMatch
from django.utils.safestring import mark_safe

from django_auxiliaries.url_signature import generate_signed_url
from ..adapters.adapter import get_media_catalogue_adapter
from ..apps import get_app_label

APP_LABEL = get_app_label()

register = template.Library()
adapter = get_media_catalogue_adapter()


@register.simple_tag(name="media_item_preview", takes_context=True)
def media_item_preview_tag(context, media_item, cell=None):
    return mark_safe(adapter.render_preview(media_item, cell))


@register.simple_tag(name="media_item", takes_context=True)
def media_item_tag(context, media_item, cell=None):
    return mark_safe(adapter.render_in_responsive_cell(media_item, cell, template_context=context))


@register.simple_tag()
def media_item_url(media_item, file_name, url_specifier=APP_LABEL + "_frontend:serve"):
    try:
        return generate_signed_url(media_item, file_name, url_specifier=url_specifier)
    except NoReverseMatch:
        raise ImproperlyConfigured(
            "'media_item_url' tag requires the " + url_specifier + " view to be configured."
        )
