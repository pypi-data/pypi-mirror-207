

from django.utils.translation import gettext_lazy
from django.shortcuts import get_object_or_404
from django.contrib.admin.utils import quote, unquote
from django.urls import reverse

from wagtail.admin.ui.tables import Column, DateColumn, UserColumn
from wagtail.admin.views.generic.models import IndexView
from wagtail.log_actions import registry as log_registry

from ..apps import get_app_label, get_media_item_model


__all__ = ['HistoryView']


APP_LABEL = get_app_label()


class HistoryView(IndexView):
    template_name = 'wagtailadmin/generic/index.html'
    page_title = gettext_lazy('Media item history')
    header_icon = 'history'
    paginate_by = 50
    columns = [
        Column('message', label=gettext_lazy("Action")),
        UserColumn('user', blank_display_name='system'),
        DateColumn('timestamp', label=gettext_lazy("Date")),
    ]

    def dispatch(self, request, media_item_pk):
        # noinspection PyPep8Naming
        MediaItemClass = get_media_item_model()

        media_item = get_object_or_404(MediaItemClass, pk=unquote(media_item_pk))

        self.object = media_item.specific

        # noinspection PyPep8Naming
        self.model = self.object.__class__

        self.app_label = self.model._meta.app_label
        self.model_name = self.model._meta.model_name

        return super().dispatch(request)

    def get_page_subtitle(self):
        return str(self.object)

    def get_index_url(self):
        return reverse(APP_LABEL + ':history', args=(quote(self.object.pk),))

    def get_queryset(self):
        return log_registry.get_logs_for_instance(self.object).prefetch_related('user__wagtail_userprofile')
