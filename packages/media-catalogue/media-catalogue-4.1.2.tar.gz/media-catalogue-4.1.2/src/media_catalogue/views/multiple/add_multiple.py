

from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_headers

from wagtail.admin.views.generic.multiple_upload import AddView as BaseAddView

from media_catalogue.form_fields import ALLOWED_EXTENSIONS
from media_catalogue.models.media_items import UploadedMediaItem
from media_catalogue.forms import get_media_item_form, get_media_item_multi_form
from media_catalogue.models.permissions import permission_policy
from media_catalogue.apps import get_app_label, get_media_item_model

from media_catalogue.views.auxiliaries import get_media_item_model_from_url_params

APP_LABEL = get_app_label()

__all__ = ['AddView']


class AddView(BaseAddView):

    # subclasses need to provide:
    # - permission_policy
    # - template_name
    # - upload_model

    # - edit_object_url_name
    # - delete_object_url_name
    # - edit_object_form_prefix
    # - context_object_name
    # - context_object_id_name

    # - edit_upload_url_name
    # - delete_upload_url_name
    # - edit_upload_form_prefix
    # - context_upload_name
    # - context_upload_id_name

    # - get_model()
    # - get_upload_form_class()
    # - get_edit_form_class()

    permission_policy = permission_policy
    template_name = APP_LABEL + '/multiple/multiple_add.html'
    upload_model = UploadedMediaItem

    edit_object_url_name = APP_LABEL + ':edit_multiple'
    delete_object_url_name = APP_LABEL + ':delete_multiple'
    edit_object_form_prefix = 'media-item'
    context_object_name = 'media_item'
    context_object_id_name = 'media_item_id'

    edit_upload_url_name = APP_LABEL + ':create_multiple_from_uploaded_media_item'
    delete_upload_url_name = APP_LABEL + ':delete_upload_multiple'
    edit_upload_form_prefix = 'uploaded-media-item'
    context_upload_name = 'uploaded_media_item'
    context_upload_id_name = 'uploaded_media_item_id'

    # noinspection PyMethodMayBeStatic
    def get_model(self):
        return self.model

    def get_upload_form_class(self):
        return get_media_item_form(self.model)

    def get_edit_form_class(self):
        return get_media_item_multi_form(self.model)

    def save_object(self, form):
        media_item = form.save(commit=False)
        media_item.created_by_user = self.request.user
        media_item.file_size = media_item.file.size
        media_item.file.seek(0)
        media_item._set_file_hash(media_item.file.read())
        media_item.file.seek(0)
        media_item.save()
        return media_item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'max_filesize': self.form.fields['file'].max_upload_size,
            'max_title_length': self.form.fields['title'].max_length,
            'allowed_extensions': ALLOWED_EXTENSIONS,
            'error_max_file_size': self.form.fields['file'].error_messages['file_too_large_unknown_size'],
            'error_accepted_file_types': self.form.fields['file'].error_messages['invalid_media_item_extension'],
            'model_opts': self.get_model()._meta
        })

        return context

    @method_decorator(vary_on_headers('X-Requested-With'))
    def dispatch(self, request, app_label, model_name):

        # noinspection PyPep8Naming
        self.model = get_media_item_model_from_url_params(app_label, model_name)

        return super().dispatch(request)