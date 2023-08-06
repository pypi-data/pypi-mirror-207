

from types import SimpleNamespace
import os

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.admin.utils import quote, unquote
from django.db import transaction
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _
from django.utils.text import capfirst
from django.utils.http import urlencode
from django.urls import reverse

from django.http import Http404

from django.views.generic.base import View

from wagtail.log_actions import log
from wagtail.log_actions import registry as log_registry
from wagtail.models import Locale, TranslatableMixin
from wagtail.admin.views.pages.utils import get_valid_next_url_from_request
from wagtail.admin import messages
from wagtail.admin.auth import PermissionPolicyChecker

from ..adapters.adapter import get_media_catalogue_adapter
from ..apps import get_app_label

from ..action_menu import MediaItemActionMenu

__all__ = ['Editor']

APP_LABEL = get_app_label()


class Editor(View):

    adapter = None
    permissions = None
    signature_key = None

    def __init__(self, adapter=None, permissions=None, **kwargs):
        super().__init__(**kwargs)

        if adapter is None:
            adapter = get_media_catalogue_adapter()

        if permissions is None:
            permissions = []

        self.adapter = adapter
        self.permissions = permissions
        self.permission_checker = PermissionPolicyChecker(self.adapter.permission_policy)

        result = self.get_inner
        f = self.permission_checker.require_any(permissions)
        self.get = f(result)

        result = self.post_inner
        f = self.permission_checker.require_any(permissions)
        self.post = f(result)

    def handle(self, request, media_item_pk):

        # Get items (filtered by user permission)
        instances = self.adapter.permission_policy.instances_user_has_any_permission_for(
            request.user, self.permissions
        )

        instances = instances.filter(pk=unquote(media_item_pk))

        if not instances:
            raise Http404()

        media_item = instances[0]

        panel = self.adapter.create_panel_for(media_item, request)

        context = SimpleNamespace()
        context.adapter_item = media_item
        context.media_item = media_item.specific
        context.media_item_class = media_item.specific_class
        context.panel = panel
        context.form_class = context.panel.get_form_class()
        context.next = get_valid_next_url_from_request(request)

        result = self.define_form(context, request)

        if result is not None:
            return result

        return self.render_to_response(request, context)

    def get_inner(self, request, media_item_pk):
        return self.handle(request, media_item_pk)

    def post_inner(self, request, media_item_pk):
        return self.handle(request, media_item_pk)

    def define_form(self, context, request):

        if request.method == 'POST':
            form = context.form_class(request.POST, request.FILES, instance=context.media_item)

            if form.is_valid():
                with transaction.atomic():
                    form.save()
                    log(instance=context.media_item, action='wagtail.edit')

                edit_url = self.adapter.edit_url_for(context.adapter_item)
                redirect_url = self.adapter.browser_url_specifier

                if context.next:
                    edit_url = f"{edit_url}?{urlencode({'next': context.next})}"
                    redirect_url = context.next

                messages.success(
                    request,
                    _("%(media_item_type)s '%(instance)s' updated.") % {
                        'media_item_type': capfirst(self.adapter.get_verbose_name()),
                        'instance': context.media_item
                    },
                    buttons=[
                        messages.button(edit_url, _('Edit again'))
                    ]
                )

                return redirect(redirect_url)
            else:
                messages.validation_error(
                    request, _("The media item could not be saved due to errors."), form
                )
        else:
            form = context.form_class(instance=context.media_item)

        context.form = form
        context.panel = context.panel.get_bound_panel(instance=context.media_item, request=request, form=form)

    def define_template_variables(self, template_name, context, request):

        template_context = dict(context.__dict__)

        latest_log_entry = log_registry.get_logs_for_instance(context.media_item).first()

        template_context.update({
            'model_opts': context.media_item_class._meta,
            'form': context.form,
            'edit_url': self.adapter.edit_url_for(context.adapter_item),
            'action_menu': MediaItemActionMenu(request, view='edit', instance=context.media_item),
            'locale': None,
            'translations': [],
            'latest_log_entry': latest_log_entry,
        })

        if getattr(settings, 'WAGTAIL_I18N_ENABLED', False) and issubclass(context.media_item_class, TranslatableMixin):
            context.update({
                'locale': context.media_item.locale,
                'translations': [
                    {
                        'locale': translation.locale,
                        'url': reverse(APP_LABEL + ':edit', args=[quote(translation.pk)])
                    }
                    for translation in context.media_item.get_translations().select_related('locale')
                ],
            })

        return template_context

    def render_to_response(self, request, context):

        template_name = APP_LABEL + '/edit.html'
        template_variables = self.define_template_variables(template_name, context, request)

        return TemplateResponse(
            request,
            template_name,
            template_variables
        )


