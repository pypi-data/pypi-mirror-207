

from types import SimpleNamespace
import os

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.admin.utils import quote, unquote
from django.db import transaction
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _, ngettext
from django.utils.text import capfirst
from django.utils.http import urlencode
from django.urls import reverse

from django.http import Http404

from django.views.generic.base import View

from wagtail.log_actions import log

from wagtail.admin.views.pages.utils import get_valid_next_url_from_request
from wagtail.admin import messages
from wagtail.admin.auth import PermissionPolicyChecker

from ..adapters.adapter import get_media_catalogue_adapter
from ..apps import get_app_label

__all__ = ['Deletion']

APP_LABEL = get_app_label()


class Deletion(View):

    adapter = None
    permissions = None
    signature_key = None

    def __init__(self, adapter=None, permissions=None, **kwargs):
        super().__init__(**kwargs)

        if adapter is None:
            adapter = get_media_catalogue_adapter()

        if permissions is None:
            permissions = ['delete']

        self.adapter = adapter
        self.permissions = permissions
        self.permission_checker = PermissionPolicyChecker(self.adapter.permission_policy)

        result = self.get_inner
        f = self.permission_checker.require_any(permissions)
        self.get = f(result)

        result = self.post_inner
        f = self.permission_checker.require_any(permissions)
        self.post = f(result)

    def handle(self, request, media_item_pk=None):

        if not self.adapter.permission_policy.user_has_permission(request.user, 'delete'):
            raise PermissionDenied

        # Get items (filtered by user permission)
        instances = self.adapter.permission_policy.instances_user_has_any_permission_for(
            request.user, self.permissions
        )

        if media_item_pk:
            instances = instances.filter(pk=unquote(media_item_pk))
        else:
            ids = request.GET.getlist('id')
            instances = instances.filter(pk__in=ids)

        if not instances:
            raise Http404()

        context = SimpleNamespace()
        context.media_items = instances
        context.count = len(instances)
        context.next = get_valid_next_url_from_request(request)

        if request.method == 'POST':
            with transaction.atomic():
                for instance in instances:
                    log(instance=instance, action='wagtail.delete')
                    self.adapter.delete_instance(instance)

            if context.count == 1:
                message_content = _("%(media_item_type)s '%(instance)s' deleted.") % {
                    'media_item_type': self.adapter.get_verbose_name(),
                    'instance': instance.title
                }
            else:
                # This message is only used in plural form, but we'll define it with ngettext so that
                # languages with multiple plural forms can be handled correctly (or, at least, as
                # correctly as possible within the limitations of verbose_name_plural...)
                message_content = ngettext(
                    "%(count)d %(media_item_type)s deleted.",
                    "%(count)d %(media_item_type)s deleted.",
                    context.count
                ) % {
                      'media_item_type': self.adapter.get_verbose_name(plural=True),
                      'count': context.count
                  }

            messages.success(request, message_content)
            return redirect(self.adapter.browser_url_specifier)

        return self.render_to_response(request, context)

    def get_inner(self, request, media_item_pk=None):
        return self.handle(request, media_item_pk)

    def post_inner(self, request, media_item_pk=None):
        return self.handle(request, media_item_pk)

    def define_template_variables(self, template_name, context, request):

        template_context = dict(context.__dict__)

        template_context.update({
            'verbose_name': self.adapter.get_verbose_name(),
            'verbose_name_plural': self.adapter.get_verbose_name(plural=True),
            'usage_url': '',
            'get_usage': None,
            'submit_url': (
                    reverse(self.adapter.browser_delete_multiple_url_specifier)
                    + '?' + urlencode([('id', media_item.pk) for media_item in context.media_items])
            ),
        })

        return template_context

    def render_to_response(self, request, context):

        template_name = APP_LABEL + '/confirm_delete.html'
        template_variables = self.define_template_variables(template_name, context, request)

        return TemplateResponse(
            request,
            template_name,
            template_variables
        )


