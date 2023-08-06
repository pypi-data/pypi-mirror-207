from django.core.exceptions import ObjectDoesNotExist

from wagtail.rich_text import EmbedHandler

from .apps import get_media_item_model
from .editor.contentstate import EMBED_TYPE

__all__ = ['MediaItemEmbedHandler']


class MediaItemEmbedHandler(EmbedHandler):
    identifier = EMBED_TYPE

    @staticmethod
    def get_model():
        return get_media_item_model()

    @classmethod
    def expand_db_attributes(cls, attrs):
        """
        Given a dict of attributes from the <embed> tag, return the real HTML
        representation for use on the front-end.
        """
        try:
            image = cls.get_instance(attrs)
        except ObjectDoesNotExist:
            return '<div alt="">'

        #image_format = get_image_format(attrs['format'])
        #return image_format.image_to_html(image, attrs.get('alt', ''))
        return '<div/>'
