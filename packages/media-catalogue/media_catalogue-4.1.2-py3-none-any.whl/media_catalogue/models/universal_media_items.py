from django.db.models.signals import post_save, pre_delete
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.dispatch import receiver

import django.db.models as models

from wagtail.search import index

from wagtail.permission_policies.base import ModelPermissionPolicy
from taggit.managers import TaggableManager
from taggit.models import TaggedItem

from ..adapters.registry import adapter_registry
from ..universal_query import UniversalMediaItemQuerySet


__all__ = ['UniversalMediaItem', 'permission_policy']


class BaseUniversalMediaItemManager(models.Manager):

    def get_queryset(self):
        return self._queryset_class(self.model).order_by('-created_at', 'id')


UniversalMediaItemManager = BaseUniversalMediaItemManager.from_queryset(UniversalMediaItemQuerySet)


class UniversalMediaItem(index.Indexed, models.Model):

    class Meta:
        verbose_name = 'Universal Media Item'
        verbose_name_plural = 'Universal Media Items'
        ordering = ['-created_at', 'id']
        index_together = [["content_type", "content_id"]]
        unique_together = [["content_type", "content_id"]]

    objects = UniversalMediaItemManager()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=False)
    content_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type', 'content_id')
    created_at = models.DateTimeField()

    tags = TaggableManager(help_text=None, blank=True, verbose_name=_('tags'))

    search_fields = [
        index.FilterField('id'),
        index.FilterField('content_type'),
        index.FilterField('content_id'),
        index.FilterField('created_at'),
    ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # noinspection PyUnresolvedReferences
        if not self.id:

            self.id = None
            self.created_at = timezone.now()

        self.adapter = adapter_registry.get_adapter_for_content_type_id(self.content_type.id) # noqa

    @cached_property
    def specific_class(self):
        """
        Return the class that this media item would be if instantiated in its
        most specific form.

        If the model class can no longer be found in the codebase, and the
        relevant ``ContentType`` has been removed by a database migration,
        the return value will be ``None``.

        If the model class can no longer be found in the codebase, but the
        relevant ``ContentType`` is still present in the database (usually a
        result of switching between git branches without running or reverting
        database migrations beforehand), the return value will be ``None``.
        """
        return self.content_type.model_class() # noqa

    @cached_property
    def specific(self):
        """
        Returns this media_item in its most specific subclassed form with all field
        values fetched from the database. The result is cached in memory.
        """
        return self.get_specific()

    def get_specific(self, deferred=False, copy_attrs=None):
        """
        .. versionadded:: 2.12

        Return this media_item in its most specific subclassed form.

        By default, a database query is made to fetch all field values for the
        specific object. If you only require access to custom methods or other
        non-field attributes on the specific object, you can use
        ``deferred=True`` to avoid this query. However, any attempts to access
        specific field values from the returned object will trigger additional
        database queries.

        If there are attribute values on this object that you wish to be copied
        over to the specific version (for example: evaluated relationship field
        values, annotations or cached properties), use `copy_attrs`` to pass an
        iterable of names of attributes you wish to be copied.

        If called on a media_item object that is already an instance of the most
        specific class (e.g. an ``EventPage``), the object will be returned
        as is, and no database queries or other operations will be triggered.

        If the media_item was originally created using a media_item type that has since
        been removed from the codebase, a generic ``MediaItem`` object will be
        returned (without any custom field values or other functionality
        present on the original class). Usually, deleting these pages is the
        best course of action, but there is currently no safe way for Wagtail
        to do that at migration time.
        """

        model_class = self.specific_class

        if model_class is None:
            # The codebase and database are out of sync (e.g. the model exists
            # on a different git branch and migrations were not applied or
            # reverted before switching branches). So, the best we can do is
            # return the media_item in it's current form.
            return self.content_object

        if isinstance(self.content_object, model_class):
            # self.content_object is already the an instance of the most specific class
            return self.content_object

        if deferred:
            # Generate a tuple of values in the order expected by __init__(),
            # with missing values substituted with DEFERRED ()
            values = tuple(
                getattr(self.content_object, f.attname, self.content_object.pk if f.primary_key else DEFERRED)  # noqa
                for f in model_class._meta.concrete_fields
            )
            # Create object from known attribute values
            specific_obj = model_class(*values)
            specific_obj._state.adding = self.content_object._state.adding  # noqa
        else:
            # Fetch object from database
            specific_obj = model_class._default_manager.get(id=self.content_object.id)  # noqa

        # Copy additional attribute values
        for attr in copy_attrs or ():
            if attr in self.content_object.__dict__:
                setattr(specific_obj, attr, getattr(self.content_object, attr))

        return specific_obj

    @staticmethod
    def media_item_post_save(instance, **kwargs):

        content_type = ContentType.objects.get_for_model(instance.__class__)

        try:
            universal_item = UniversalMediaItem.objects.get(content_type=content_type, content_id=instance.id)

            if universal_item.id is None:
                universal_item.save()

        except UniversalMediaItem.DoesNotExist:
            universal_item = UniversalMediaItem(content_type=content_type, content_id=instance.id)

            if instance.id is not None:
                universal_item.save()

        return universal_item

    @staticmethod
    def media_item_pre_delete(instance, **kwargs):

        content_type = ContentType.objects.get_for_model(instance.__class__)

        try:
            universal_item = UniversalMediaItem.objects.get(content_type=content_type, content_id=instance.id)
            universal_item.delete()
        except UniversalMediaItem.DoesNotExist:
            pass

    @staticmethod
    def tag_post_save(instance, **kwargs):

        content_type = ContentType.objects.get_for_id(instance.content_type_id)
        universal_type = ContentType.objects.get_for_model(UniversalMediaItem)

        if content_type is universal_type:
            return

        try:
            universal_item = UniversalMediaItem.objects.get(content_type=content_type, content_id=instance.object_id)
        except UniversalMediaItem.DoesNotExist:
            return

        shadow_item = TaggedItem(content_type_id=universal_type.id,
                                 object_id=universal_item.id,
                                 tag_id=instance.tag_id)

        shadow_item.save()

    @staticmethod
    def tag_pre_delete(instance, **kwargs):

        content_type = ContentType.objects.get_for_id(instance.content_type_id)
        universal_type = ContentType.objects.get_for_model(UniversalMediaItem)

        if content_type is universal_type:
            return

        try:
            universal_item = UniversalMediaItem.objects.get(content_type=content_type, content_id=instance.object_id)
        except UniversalMediaItem.DoesNotExist:
            return

        shadow_item = TaggedItem.objects.all().get(content_type_id=universal_type.id, object_id=universal_item.id, tag_id=instance.tag_id)
        shadow_item.delete()

        pass


permission_policy = ModelPermissionPolicy(
    UniversalMediaItem,
    auth_model=UniversalMediaItem,
    # owner_field_name='created_by_user'
)


adapter_registry.register_signal_handler(post_save, UniversalMediaItem.media_item_post_save)
adapter_registry.register_signal_handler(pre_delete, UniversalMediaItem.media_item_pre_delete)


UniversalMediaItem.tag_post_save = receiver(post_save, sender=TaggedItem)(UniversalMediaItem.tag_post_save)
UniversalMediaItem.tag_pre_delete = receiver(pre_delete, sender=TaggedItem)(UniversalMediaItem.tag_pre_delete)
