from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from wagtail.admin import widgets
from .media_item_bulk_action import MediaItemBulkAction

from media_catalogue.apps import get_app_label

APP_LABEL = get_app_label()


class TagForm(forms.Form):
    tags = forms.Field(widget=widgets.AdminTagWidget)


class AddTagsBulkAction(MediaItemBulkAction):

    display_name = _("Tag")
    action_type = "add_tags"
    aria_label = _("Add tags to the selected media items")
    template_name = APP_LABEL + "/bulk_actions/confirm_bulk_add_tags.html"
    action_priority = 20
    form_class = TagForm

    def check_perm(self, media_item):
        return self.permission_policy.user_has_permission_for_instance(self.request.user, 'change', media_item)

    def get_execution_context(self):
        context = super(AddTagsBulkAction, self).get_execution_context()
        context.update({
            'tags': self.cleaned_form.cleaned_data['tags'].split(',')
        })
        return context

    @classmethod
    def execute_action(cls, media_items, tags=[], action=None, **kwargs):
        num_parent_objects = 0

        if not tags:
            return

        for media_item in media_items:
            num_parent_objects += 1
            media_item.specific.tags.add(*tags)
        return num_parent_objects, 0

    def get_success_message(self, num_parent_objects, num_child_objects):
        return ngettext(
            "New tags have been added to %(num_parent_objects)d media item",
            "New tags have been added to %(num_parent_objects)d media items",
            num_parent_objects
        ) % {
            'num_parent_objects': num_parent_objects
        }
