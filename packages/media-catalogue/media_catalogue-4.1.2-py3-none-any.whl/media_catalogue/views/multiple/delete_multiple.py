
from wagtail.admin.views.generic.multiple_upload import DeleteView as BaseDeleteView
from media_catalogue.models.permissions import permission_policy
from media_catalogue.apps import get_app_label, get_media_item_model

MEDIA_CATALOGUE_APP_LABEL = get_app_label()

__all__ = ['DeleteView']


class DeleteView(BaseDeleteView):
    permission_policy = permission_policy
    pk_url_kwarg = 'media_item_pk'
    context_object_id_name = 'media_item_pk'

    # noinspection PyMethodMayBeStatic
    def get_model(self):
        return get_media_item_model()

