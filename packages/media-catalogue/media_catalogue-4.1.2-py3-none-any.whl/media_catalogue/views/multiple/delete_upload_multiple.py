
from wagtail.admin.views.generic.multiple_upload import DeleteUploadView as BaseDeleteUploadView

from media_catalogue.models.media_items import UploadedMediaItem
from media_catalogue.apps import get_app_label

MEDIA_CATALOGUE_APP_LABEL = get_app_label()

__all__ = ['DeleteUploadView']


class DeleteUploadView(BaseDeleteUploadView):
    upload_model = UploadedMediaItem
    upload_pk_url_kwarg = 'uploaded_media_item_id'
