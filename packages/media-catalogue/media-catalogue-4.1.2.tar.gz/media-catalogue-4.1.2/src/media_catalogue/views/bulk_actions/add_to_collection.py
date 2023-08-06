from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from .media_item_bulk_action import MediaItemBulkAction

from media_catalogue.apps import get_app_label

APP_LABEL = get_app_label()


class CollectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        adapter = kwargs.pop('adapter', None)
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['collection'] = forms.ModelChoiceField(
            queryset=adapter.permission_policy.collections_user_has_permission_for(user, 'add')
        )


class AddToCollectionBulkAction(MediaItemBulkAction):

    display_name = _("Add to collection")
    action_type = "add_to_collection"
    aria_label = _("Add selected media items to collection")
    template_name = APP_LABEL + "/bulk_actions/confirm_bulk_add_to_collection.html"
    action_priority = 30
    form_class = CollectionForm
    collection = None

    def check_perm(self, media_item):
        return self.permission_policy.user_has_permission_for_instance(self.request.user, 'change', media_item)

    def get_form_kwargs(self):
        return {
            **super().get_form_kwargs(),
            'adapter': self.adapter,
            'user': self.request.user
        }

    def get_execution_context(self):
        context = super(AddToCollectionBulkAction, self).get_execution_context()
        context.update({
            'collection': self.cleaned_form.cleaned_data['collection']
        })
        return context

    @classmethod
    def execute_action(cls, media_items, action=None, collection=None, **kwargs):
        if collection is None:
            return

        object_ids = [obj.pk for obj in media_items]
        media_items = action.get_queryset(action.model, object_ids)
        num_parent_objects = media_items.update(collection=collection)
        return num_parent_objects, 0

    def get_success_message(self, num_parent_objects, num_child_objects):
        collection = self.cleaned_form.cleaned_data['collection']
        return ngettext(
            "%(num_parent_objects)d media item has been added to %(collection)s",
            "%(num_parent_objects)d media items have been added to %(collection)s",
            num_parent_objects
        ) % {
            'num_parent_objects': num_parent_objects,
            'collection': collection.name
        }
