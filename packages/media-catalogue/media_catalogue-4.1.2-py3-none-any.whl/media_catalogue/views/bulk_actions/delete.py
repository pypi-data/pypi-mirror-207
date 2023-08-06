from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from .media_item_bulk_action import MediaItemBulkAction

from media_catalogue.apps import get_app_label

APP_LABEL = get_app_label()


class DeleteBulkAction(MediaItemBulkAction):

    display_name = _("Delete")
    action_type = "delete"
    aria_label = _("Delete selected media items")
    template_name = APP_LABEL + "/bulk_actions/confirm_bulk_delete.html"
    action_priority = 100
    classes = {'serious'}

    def check_perm(self, document):
        return self.permission_policy.user_has_permission_for_instance(self.request.user, 'delete', document)

    @classmethod
    def execute_action(cls, media_items, action=None, **kwargs):
        num_parent_objects = len(media_items)
        object_ids = [obj.pk for obj in media_items]
        media_items = action.get_queryset(action.model, object_ids)
        action.adapter.bulk_delete_instances(media_items)
        return num_parent_objects, 0

    def get_success_message(self, num_parent_objects, num_child_objects):
        return ngettext(
            "%(num_parent_objects)d media item has been deleted",
            "%(num_parent_objects)d media items have been deleted",
            num_parent_objects
        ) % {
            'num_parent_objects': num_parent_objects
        }
