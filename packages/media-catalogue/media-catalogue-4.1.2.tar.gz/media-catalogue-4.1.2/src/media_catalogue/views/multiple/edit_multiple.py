
from wagtail.admin.views.generic.multiple_upload import EditView as BaseEditView

from wagtail.search.backends import get_search_backends

from media_catalogue.forms import get_media_item_multi_form
from media_catalogue.models.permissions import permission_policy
from media_catalogue.apps import get_app_label, get_media_item_model

MEDIA_CATALOGUE_APP_LABEL = get_app_label()

__all__ = ['EditView']


class EditView(BaseEditView):
    permission_policy = permission_policy
    pk_url_kwarg = 'media_item_id'
    edit_object_form_prefix = 'media-item'
    context_object_name = 'media_item'
    context_object_id_name = 'media_item_id'
    edit_object_url_name = MEDIA_CATALOGUE_APP_LABEL + ':edit_multiple'
    delete_object_url_name = MEDIA_CATALOGUE_APP_LABEL + ':delete_multiple'

    # noinspection PyMethodMayBeStatic
    def get_model(self):
        return get_media_item_model()

    def get_edit_form_class(self):
        return get_media_item_multi_form(self.model)

    def save_object(self, form):
        form.save()

        # Reindex the media_item to make sure all tags are indexed
        for backend in get_search_backends():
            backend.add(self.object)
