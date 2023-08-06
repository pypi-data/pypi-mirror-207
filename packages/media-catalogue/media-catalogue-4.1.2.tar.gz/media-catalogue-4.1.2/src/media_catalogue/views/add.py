
from types import SimpleNamespace

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _
from django.utils.text import capfirst
from django.contrib.admin.utils import quote, unquote

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from wagtail.models import Locale, TranslatableMixin
from wagtail.log_actions import log

from wagtail.admin import messages

from ..apps import get_app_label
from ..models.permissions import permission_policy
from ..action_menu import MediaItemActionMenu

from .auxiliaries import get_media_item_model_from_url_params
from ..adapters.adapter import get_media_catalogue_adapter

__all__ = ['media_type_selection', 'add']

APP_LABEL = get_app_label()

"""
permission_checker = PermissionPolicyChecker(permission_policy)


def user_can_edit_media_item_type(user, media_item_class):
    return permission_policy.user_has_permission(user, 'edit')


@permission_checker.require('add')
"""


def media_type_selection(request, add_multiple=False):

    adapter = get_media_catalogue_adapter()

    def create_model_choice(url_specifier, url_args, model):

        result = SimpleNamespace()
        result.meta = model._meta
        result.url = reverse(url_specifier, args=url_args)

        return result

    model_selection = [create_model_choice(*specifier) for specifier in adapter.add_url_specifiers]

    if model_selection:
        return TemplateResponse(request, APP_LABEL + '/media_type_selection.html', {
            'model_selection': sorted(
                model_selection, key=lambda x: x.meta.verbose_name.lower())})
    else:
        raise PermissionDenied


# @permission_checker.require('add')

def add(request, app_label, model_name):

    # noinspection PyPep8Naming
    MediaItemClass = get_media_item_model_from_url_params(app_label, model_name)

    instance = MediaItemClass(created_by_user=request.user)

    # Set locale of the new instance
    if issubclass(MediaItemClass, TranslatableMixin):
        selected_locale = request.GET.get('locale')
        if selected_locale:
            instance.locale = get_object_or_404(Locale, language_code=selected_locale)
        else:
            instance.locale = Locale.get_default()

    # Make edit handler
    panel = MediaItemClass.edit_handler
    panel = panel.bind_to_model(MediaItemClass)  # panel.bind_to(model=MediaItemClass, request=request)
    form_class = panel.get_form_class()

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            with transaction.atomic():
                form.save()
                log(instance=instance, action='wagtail.create')

            messages.success(
                request,
                _("%(media_item_type)s '%(instance)s' created.") % {
                    'media_item_type': capfirst(MediaItemClass._meta.verbose_name),
                    'instance': instance
                },
                buttons=[
                    messages.button(reverse(
                        APP_LABEL + ':edit', args=(quote(instance.pk),)
                    ), _('Edit'))
                ]
            )

            url_query = ''
            if isinstance(instance, TranslatableMixin) and instance.locale is not Locale.get_default():
                url_query = '?locale=' + instance.locale.language_code

            return redirect(reverse(APP_LABEL + ':index') + url_query)

        else:
            messages.validation_error(
                request, _("The media item could not be created due to errors."), form
            )
    else:
        form = form_class(instance=instance)

    panel = panel.get_bound_panel(instance=instance, request=request, form=form)

    # noinspection PyProtectedMember
    context = {
        'model_opts': MediaItemClass._meta,
        'panel': panel,
        'form': form,
        'action_menu': MediaItemActionMenu(request, view='create', model=MediaItemClass),
        'locale': None,
        'translations': [],
    }

    if getattr(settings, 'WAGTAIL_I18N_ENABLED', False) and issubclass(MediaItemClass, TranslatableMixin):
        context.update({
            'locale': instance.locale,
            'translations': [
                {
                    'locale': locale,
                    'url': reverse(APP_LABEL + ':add', args=[app_label, model_name]) + '?locale=' + locale.language_code
                }
                for locale in Locale.objects.all().exclude(id=instance.locale.id)
            ],
        })

    return TemplateResponse(request, APP_LABEL + '/create.html', context)
