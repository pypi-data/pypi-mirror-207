
from functools import lru_cache

from django.contrib.admin.utils import quote
from django.forms import Media
from django.template.loader import get_template, render_to_string
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail.admin.ui.components import Component
from wagtail import hooks
from wagtail.snippets.permissions import get_permission_name

from .apps import get_app_label

APP_LABEL = get_app_label()

__all__ = ['MediaItemActionMenu', 'ActionMenuItem', 'get_base_media_item_action_menu_items']


class ActionMenuItem(Component):
    """Defines an item in the actions drop-up on the snippet creation/edit view"""
    order = 100  # default order index if one is not specified on init
    template_name = APP_LABEL + '/action_menu/menu_item.html'
    template = None  # RemovedInWagtail217Warning

    label = ''
    name = None
    classname = ''
    icon_name = ''

    def __init__(self, order=None):
        if order is not None:
            self.order = order

    def is_shown(self, context):
        """
        Whether this action should be shown on this request; permission checks etc should go here.

        request = the current request object

        context = dictionary containing at least:
            'view' = 'create' or 'edit'
            'model' = the model of the snippet being created/edited
            'instance' (if view = 'edit') = the snippet being edited
        """

        return True

    def get_context_data(self, parent_context):
        """Defines context for the template, overridable to use more data"""
        context = parent_context.copy()
        url = self.get_url(parent_context)

        context.update({
            'label': self.label,
            'url': url,
            'name': self.name,
            'classname': self.classname,
            'icon_name': self.icon_name,
            'request': parent_context['request'],
        })

        return context

    def get_url(self, parent_context):
        return None

    def render_html(self, parent_context=None):

        context_data = self.get_context_data(parent_context)

        template = get_template(self.template_name)
        return template.render(context_data)


class DeleteMenuItem(ActionMenuItem):
    name = 'action-delete'
    label = _("Delete")
    icon_name = 'bin'
    classname = 'action-secondary'

    def is_shown(self, context):
        delete_permission = get_permission_name('delete', context['model'])

        return (
            context['view'] == 'edit'
            and context['request'].user.has_perm(delete_permission)
        )

    def get_url(self, context):
        return reverse(APP_LABEL + ':delete', args=[
            # context['model']._meta.app_label,
            # context['model']._meta.model_name,
            # quote(context['instance'].pk)
            context['instance'].id
        ])


class SaveMenuItem(ActionMenuItem):
    name = 'action-save'
    label = _("Save")
    template_name = APP_LABEL + '/action_menu/save.html'


@lru_cache(maxsize=None)
def get_base_media_item_action_menu_items(model):

    """
    Retrieve the global list of menu items for the media item action menu,
    which may then be customised on a per-request basis
    """

    menu_items = [
        SaveMenuItem(order=0),
        DeleteMenuItem(order=10),
    ]

    for hook in hooks.get_hooks('register_media_item_action_menu_item'):
        action_menu_item = hook(model)
        if action_menu_item:
            menu_items.append(action_menu_item)

    return menu_items


class MediaItemActionMenu:
    template = APP_LABEL + '/action_menu/menu.html'

    def __init__(self, request, **kwargs):
        self.request = request
        self.context = kwargs
        self.context['request'] = request
        self.menu_items = []

        if 'instance' in self.context:
            self.context['model'] = self.context['instance'].__class__

        for menu_item in get_base_media_item_action_menu_items(self.context['model']):
            is_shown = menu_item.is_shown(self.context)

            if is_shown:
                self.menu_items.append(menu_item)

        self.menu_items.sort(key=lambda item: item.order)

        for hook in hooks.get_hooks('construct_media_item_action_menu'):
            hook(self.menu_items, self.request, self.context)

        try:
            self.default_item = self.menu_items.pop(0)
        except IndexError:
            self.default_item = None

    def render_html(self):
        rendered_menu_items = []

        for menu_item in self.menu_items:
            rendered_menu_items.append(menu_item.render_html(self.context))

        rendered_default_item = self.default_item.render_html(self.context)

        return render_to_string(self.template, {
            'default_menu_item': rendered_default_item,
            'show_menu': bool(self.menu_items),
            'rendered_menu_items': rendered_menu_items,
        }, request=self.request)

    @cached_property
    def media(self):
        media = Media()
        for item in self.menu_items:
            media += item.media
        return media
