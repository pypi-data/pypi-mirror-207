
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import BaseViewRestriction

from .audit_log import MediaItemLogEntry

__all__ = ['MediaItemViewRestriction']


class MediaItemViewRestriction(BaseViewRestriction):

    media_item = models.ForeignKey(
        'MediaItem', verbose_name=_('Media Item'), related_name='view_restrictions', on_delete=models.CASCADE
    )

    passed_view_restrictions_session_key = 'passed_view_restrictions'

    class Meta:
        verbose_name = _('media item view restriction')
        verbose_name_plural = _('media item view restrictions')

    def __init__(self, *args, **kwargs):

        super(MediaItemViewRestriction).__init__(*args, log_entry_class=MediaItemLogEntry, **kwargs)
        self.passed_view_restrictions_session_key = 'passed_view_restrictions'

    def save(self, user=None, **kwargs):
        return super().save(user,
                            specific_instance=self.media_item.specific,  # noqa
                            **kwargs)

    def delete(self, user=None, **kwargs):
        return super().delete(user,
                              specific_instance=self.media_item.specific,  # noqa
                              **kwargs)
