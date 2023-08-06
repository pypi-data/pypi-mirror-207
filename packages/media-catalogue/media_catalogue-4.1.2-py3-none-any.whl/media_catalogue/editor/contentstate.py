from draftjs_exporter.dom import DOM

from wagtail.admin.rich_text.converters.contentstate_models import Entity
from wagtail.admin.rich_text.converters.html_to_contentstate import AtomicBlockEntityElementHandler

from wagtail.images.formats import get_image_format
from wagtail.images.shortcuts import get_rendition_or_not_found

from ..apps import get_media_item_model
from ..formats import get_media_item_format

__all__ =['MediaItemElementHandler', 'ContentstateMediaItemConversionRule', 'ENTITY_TYPE', 'FEATURE_NAME', 'EMBED_TYPE']

EMBED_TYPE = 'media_item'
FEATURE_NAME = 'media_catalogue.media_item'
ENTITY_TYPE = 'media_catalogue.MEDIA_ITEM'



def media_item_entity(props):
    """
    Helper to construct elements of the form
    <embed alt="Right-aligned image" embedtype="image" format="right" id="1"/>
    when converting from contentstate data
    """
    return DOM.create_element('embed', {
        'embedtype': EMBED_TYPE,
        'format': props.get('format'),
        'id': props.get('id')
    })


class MediaItemElementHandler(AtomicBlockEntityElementHandler):

    """
    Converting a media item entity from database representation
    to contentstate
    """

    def create_entity(self, name, attrs, state, contentstate):

        MediaItem = get_media_item_model()

        try:
            media_item = MediaItem.objects.get(id=attrs['id'])

            """
            image_format = get_media_item_format(attrs['format'])
            rendition = get_rendition_or_not_found(media_item, image_format.filter_spec)
            src = rendition.url
            """

            src = 'hello:'
        except MediaItem.DoesNotExist:
            src = ''

        return Entity(ENTITY_TYPE, 'IMMUTABLE', {
            'id': attrs['id'],
            'src': src,
            'format': attrs['format']
        })


ContentstateMediaItemConversionRule = {
    'from_database_format': {
        'embed[embedtype=' + EMBED_TYPE + ']': MediaItemElementHandler(),
    },
    'to_database_format': {
        'entity_decorators': {ENTITY_TYPE: media_item_entity}
    }
}
