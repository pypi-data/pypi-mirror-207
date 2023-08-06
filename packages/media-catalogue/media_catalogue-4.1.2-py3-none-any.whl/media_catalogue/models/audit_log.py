# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property

from wagtail.models import BaseLogEntryManager, BaseLogEntry

from ..apps import get_app_label

__all__ = ['MediaItemLogEntry']


class MediaItemLogEntryManager(BaseLogEntryManager):

    def log_action(self, instance, action, **kwargs):
        kwargs.update(media_item=instance)
        return super().log_action(instance, action, **kwargs)


class MediaItemLogEntry(BaseLogEntry):

    class Meta:
        ordering = ['-timestamp', '-id']
        verbose_name = _('media item log entry')
        verbose_name_plural = _('media item log entries')

    media_item = models.ForeignKey(
        get_app_label() + '.MediaItem',
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name='+'
    )

    objects = MediaItemLogEntryManager()

    def __str__(self):
        return "MediaItemLogEntry %d: '%s' on '%s' with id %s" % (
            self.pk, self.action, self.object_verbose_name(),
            self.media_item_id  # noqa
        )

    @cached_property
    def object_id(self):
        return self.media_item_id  # noqa

