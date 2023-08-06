
from django.conf import settings

from wagtail_content_admin.blocks import ContentBlock, ContentBlockValue, register_content_block

from querykit.base import *
from querykit.value_types import *
from querykit.value_sources import *
from querykit.forms import PickerFactory

from .apps import get_app_label


__all__ = ['MediaItemChooserBlock', 'MediaItemChooserBlockValue', 'MediaItemsBlock']

APP_LABEL = get_app_label()

default_adapter = None
generalize = None


def configure_chooser_media_item(item, instance):

    global default_adapter

    if default_adapter is None:
        from .adapters.adapter import get_media_catalogue_adapter
        default_adapter = get_media_catalogue_adapter()

    default_adapter.configure_frontend_item(item, instance)


def create_media_item_query_parameters():
    fp_factory = PickerFactory()

    parameters = [
        ResultSliceParameter(
               identifier='p',
               widget_factory=None),

        OrderParameter(
               identifier='sort_by',
               label='Sort By',
               widget_factory=None),

        SliceSizeParameter(
               identifier='per_page',
               label='Per Page',
               widget_factory=None),

        Filter(identifier='title',
               label='Title',
               value_source=PathValueSource(value_type=TextType, path='title'),
               widget_factory=fp_factory),
        Filter(identifier='keyword',
               label='Keyword',
               value_source=PathValueSource(value_type=TextType, path='tags.slug', label_path='tags.name'),
               widget_factory=fp_factory)
    ]

    return parameters


class MediaItemsBlock(ContentBlock):

    class Meta:

        verbose_item_name = "Media Item"
        verbose_item_name_plural = "Media Items"

        chooser_url = APP_LABEL + ':chooser'
        configure_function_name = APP_LABEL + '.blocks.configure_chooser_media_item'
        max_num_choices = None
        chooser_prompts = {
            'add': 'Add Media Item',
            'replace': 'Replace Media Item'
        }

        chooser_filter = None

        query_field_choices = [
            ('publication_title', 'Title'),
            ('container_title', 'Container Title'),
            ('year', 'Year'),
            ('tags__name', 'Tag Name'),
            ('doi', 'DOI'),
            ('isbn', 'ISBN')
        ]
        query_slice_size = 25
        query_parameters = create_media_item_query_parameters()
        query_form_classname = settings.MEDIA_CATALOGUE_MEDIA_ITEMS_QUERY_FORM_CLASSNAME

    def __init__(self, **kwargs):
        super().__init__(target_model=APP_LABEL + (".universalmediaitem" if settings.MEDIA_CATALOGUE_UNIFY_MEDIA else ".mediaitem"), **kwargs) # noqa


register_content_block(APP_LABEL, "mediaitems", MediaItemsBlock, [], {},
                       item_type=APP_LABEL + (".universalmediaitem" if settings.MEDIA_CATALOGUE_UNIFY_MEDIA else ".mediaitem"))


MediaItemChooserBlockValue = ContentBlockValue


class MediaItemChooserBlock(MediaItemsBlock):

    class Meta:
        default_block_name = MediaItemsBlock._meta_class.chooser_block_name
        query_block_class = None
