
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.admin.utils import quote, unquote
from django.template.response import TemplateResponse

from ..apps import get_media_item_model, get_app_label

APP_LABEL = get_app_label()

# USAGE_PAGE_SIZE = getattr(settings, 'MEDIA_CATALOGUE_USAGE_PAGE_SIZE', 20)
USAGE_PAGE_SIZE = 20

__all__ = ['usage']


def usage(request, media_item_pk):
    media_item = get_object_or_404(get_media_item_model(), pk=unquote(media_item_pk))

    paginator = Paginator(media_item.get_usage(), per_page=USAGE_PAGE_SIZE)
    used_by = paginator.get_page(request.GET.get('p'))

    return TemplateResponse(request, APP_LABEL + "/usage.html", {
        'media_item': media_item,
        'used_by': used_by
    })
