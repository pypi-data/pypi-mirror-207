import os.path

from wagtail.admin.views.generic.multiple_upload import \
    CreateFromUploadView as BaseCreateFromUploadView

from wagtail.search.backends import get_search_backends

from media_catalogue.models.media_items import UploadedMediaItem
from media_catalogue.forms import get_media_item_form, get_media_item_multi_form
from media_catalogue.apps import get_app_label, get_media_item_model

MEDIA_CATALOGUE_APP_LABEL = get_app_label()

__all__ = ['CreateFromUploadedMediaItemView']


class CreateFromUploadedMediaItemView(BaseCreateFromUploadView):
    edit_upload_url_name = MEDIA_CATALOGUE_APP_LABEL + ':create_multiple_from_uploaded_media_item'
    delete_upload_url_name = MEDIA_CATALOGUE_APP_LABEL + ':delete_upload_multiple'
    upload_model = UploadedMediaItem
    upload_pk_url_kwarg = 'uploaded_media_item_id'
    edit_upload_form_prefix = 'uploaded-media-item'
    context_object_id_name = 'media_item_id'
    context_upload_name = 'uploaded_media_item'

    # noinspection PyMethodMayBeStatic
    def get_model(self):
        return get_media_item_model()

    def get_edit_form_class(self):
        return get_media_item_multi_form(self.model)

    def save_object(self, form):
        # assign the file content from uploaded_media_item to the media_item object, to ensure it gets saved to
        # storage

        self.object.file.save(os.path.basename(self.upload.file.name), self.upload.file.file, save=False)
        self.object.created_by_user = self.request.user
        self.object.file_size = self.object.file.size
        self.object.file.open()
        self.object.file.seek(0)
        self.object._set_file_hash(self.object.file.read())
        self.object.file.seek(0)
        form.save()

        # Reindex the media_item to make sure all tags are indexed
        for backend in get_search_backends():
            backend.add(self.object)
