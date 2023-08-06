# -*- coding: utf-8 -*-

import logging

from django.db import models, DEFAULT_DB_ALIAS

from django.urls import reverse
from django.conf import settings
from django.core.files.storage import default_storage
from django.db.models.signals import pre_delete, post_delete

from django.utils.translation import gettext_lazy as _
from django.utils.text import capfirst
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.utils import quote

from wagtail.admin.models import get_object_usage
from wagtail.admin.panels import FieldPanel, InlinePanel, ObjectList, extract_panel_definitions_from_model_class
from wagtail.coreutils import camelcase_to_underscore

from wagtail.models import CollectionMember
from wagtail.search import index
from wagtail.log_actions import log
from wagtail import hooks

from modelcluster.models import ClusterableModel

from taggit.managers import TaggableManager

from wagtail_attachments.models.mixins import AttachableMixin, StorageMixin, SpecificMixin
from wagtail_attachments.models import create_model_attachment_class

from .mixins import ChangeScopeMixin, PreviewGeneratorMixin
from .audit_log import MediaItemLogEntry
from .view_restrictions import MediaItemViewRestriction
from .media_item_fields import MediaItemField

from ..query import MediaItemQuerySet
from ..apps import get_app_label


__all__ = ['get_media_item_models', 'MediaItemClass', 'MediaItemManager', 'MediaItem', 'register_media_item',
           'MediaItemAttachment']

APP_LABEL = get_app_label()


logger = logging.getLogger('wagtail.core')

MEDIA_ITEM_MODELS = dict()


def media_item_usage_url(args):
    """
    :param args: [app_label, model_name, pk]
    :return: url
    """
    return reverse(get_app_label() + ':usage', args=args)


def media_item_serve_url(args):
    return reverse(get_app_label() + '_serve', args=args)


def get_media_item_models():
    return MEDIA_ITEM_MODELS.values()


def register_media_item(model):

    # noinspection PyProtectedMember
    if model._meta.label_lower not in MEDIA_ITEM_MODELS:
        # noinspection PyProtectedMember
        MEDIA_ITEM_MODELS[model._meta.label_lower] = model

        from .permissions import permission_policy
        from ..adapters.adapter import MediaCatalogueAdapter

        add_url_specifiers = [(APP_LABEL + ':' + MediaCatalogueAdapter.browser_add_url_name, (model._meta.app_label, model._meta.model_name), model)]
        adapter = MediaCatalogueAdapter(model, permission_policy=permission_policy, add_url_specifiers=add_url_specifiers)
        hooks.register('register_media_catalogue_adapter', adapter)

        pre_delete.connect(model.will_be_deleted, sender=model)
        post_delete.connect(model.was_deleted, sender=model)

    else:
        # noinspection PyProtectedMember
        raise RuntimeError(
            "Conflicting media item models: %s and %s." %
            (MEDIA_ITEM_MODELS[model._meta.label_lower]._meta.label_lower, model._meta.label_lower))

    return model


def get_default_media_item_content_type():
    """
    Returns the content type to use as a default for media items whose content type
    has been deleted.
    """
    return ContentType.objects.get_for_model(MediaItem)


class BaseMediaItemManager(models.Manager):

    def get_queryset(self):
        return self._queryset_class(self.model).order_by('-created_at', 'id')


MediaItemManager = BaseMediaItemManager.from_queryset(MediaItemQuerySet)


class MediaItemClass(models.base.ModelBase):

    # noinspection PyUnresolvedReferences
    def __init__(cls, name, bases, attrs):

        # module = attrs.get('__module__')
        # app_config = apps.get_containing_app_config(module)

        super(MediaItemClass, cls).__init__(name, bases, attrs)

        if not hasattr(cls, '_meta'):
            cls._meta = None

        if 'template' not in attrs:
            # Define a default template path derived from the app name and model name
            cls.template = "%s/%s.html" % (cls._meta.app_label, camelcase_to_underscore(name))

        if 'ajax_template' not in attrs:
            cls.ajax_template = None

        # All pages should be creatable unless explicitly set otherwise.
        # This attribute is not inheritable.
        if 'is_creatable' not in attrs:
            cls.is_creatable = not cls._meta.abstract

        if not cls._meta.abstract and cls.__name__ != 'MediaItem':
            # register this type in the list of media_item content types
            register_media_item(cls)

    @property
    def edit_handler(self):

        panels = list(extract_panel_definitions_from_model_class(self))

        # get_attachment_range is a class property defined on MediaItem
        # noinspection PyUnresolvedReferences
        attachment_range = self.get_attachment_range()

        # Use InlinePanel as no 'attachments' field exists on MediaItem

        attachment_panel = InlinePanel('attachments', label="Attachments",
                                       min_num=attachment_range[0], max_num=attachment_range[1])

        panels.append(attachment_panel)

        panel = ObjectList(panels)
        return panel


def get_upload_to(instance, filename):
    return instance.content_path(filename)


# List Mixins first

class AbstractMediaItem(ChangeScopeMixin,
                        SpecificMixin,
                        StorageMixin,
                        AttachableMixin,
                        PreviewGeneratorMixin,
                        index.Indexed,
                        CollectionMember,
                        ClusterableModel):

    """
    Abstract superclass for MediaItem. According to Django's inheritance rules, managers set on
    abstract models are inherited by subclasses, but managers set on concrete models that are extended
    via multi-table inheritance are not. We therefore need to attach MediaItemManager to an abstract
    superclass to ensure that it is retained by subclasses of MediaItem.
    """

    objects = MediaItemManager()

    class Meta:
        abstract = True  # Flag this as an abstract model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MediaItem(AbstractMediaItem, metaclass=MediaItemClass):

    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        help_text=_("The media item title as you'd like it to be seen by the public")
    )

    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        default=None,
        editable=False)

    created_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('created by user'),
        null=True,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL
    )

    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('content type'),
        related_name='media_items',
        on_delete=models.SET(get_default_media_item_content_type),
        editable=False
    )

    live = models.BooleanField(verbose_name=_('live'), default=True, editable=False)

    tags = TaggableManager(help_text=None, blank=True, verbose_name=_('tags'))

    search_description = models.TextField(verbose_name=_('search description'), blank=True)

    go_live_at = models.DateTimeField(
        verbose_name=_("go live date/time"),
        blank=True,
        null=True
    )

    expire_at = models.DateTimeField(
        verbose_name=_("expiry date/time"),
        blank=True,
        null=True
    )

    expired = models.BooleanField(verbose_name=_('expired'), default=False, editable=False)

    first_published_at = models.DateTimeField(
        verbose_name=_('first published at'),
        blank=True,
        null=True,
        db_index=True
    )

    last_published_at = models.DateTimeField(
        verbose_name=_('last published at'),
        null=True,
        editable=False
    )

    search_fields = CollectionMember.search_fields + [
        index.SearchField('title', partial_match=True, boost=2),
        index.AutocompleteField('title'),
        index.FilterField('title'),
        index.FilterField('id'),
        index.FilterField('live'),

        index.RelatedFields('tags', [
            index.SearchField('name', partial_match=True, boost=10),
            index.AutocompleteField('name'),
        ]),
        index.FilterField('created_by_user'),
        index.FilterField('created_at'),
        index.FilterField('content_type'),
        index.FilterField('first_published_at'),
        index.FilterField('last_published_at'),
        # index.FilterField('locale'),
        # index.FilterField('translation_key'),
    ]

    # Do not allow plain MediaItem instances to be created through the Wagtail admin
    is_creatable = True

    # Define the maximum number of instances this media_item type can have. Default to unlimited.
    max_count = None

    # An array of additional field names that will not be included when a Page is copied.
    exclude_fields_in_copy = []
    default_exclude_fields_in_copy = ['id', 'index_entries']

    # Define these attributes early to avoid masking errors. (Issue #3078)
    # The canonical definition is in wagtailadmin.edit_handlers.

    panels = [
        FieldPanel('title'),
        FieldPanel('collection'),
        FieldPanel('tags')
    ]

    # storage_directory = 'items'

    admin_form_fields = (
        'title',
        'collection',
        'tags',
    )

    @property
    def admin_display_title(self):
        return self.title

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # noinspection PyUnresolvedReferences
        if not self.id:

            self.id = None

            # this model is being newly created
            # rather than retrieved from the db;
            # noinspection PyUnresolvedReferences
            if not self.content_type_id:

                # set content type to correctly represent the model class
                # that this was created as
                self.content_type_id = ContentType.objects.get_for_model(self).id

            self.created_at = timezone.now()

    # noinspection PyUnusedLocal
    def attachment_saved(self, attachment_pk):
        self.did_change()

    # noinspection PyUnusedLocal
    def attachment_deleted(self, attachment_pk):
        self.did_change()

    def get_usage(self):
        return get_object_usage(self)

    @property
    def usage_url(self):
        return media_item_usage_url(args=(self._meta.app_label, self._meta.model_name, quote(self.pk)))

    def get_template_path(self):
        return getattr(self, "template_path", None)

    def is_editable_by_user(self, user):
        from media_catalogue.models import permission_policy
        return permission_policy.user_has_permission_for_instance(user, 'change', self)

    def __str__(self):
        return self.title

    def full_clean(self, *args, **kwargs):
        # Apply fixups that need to happen before per-field validation occurs

        # Set the locale
        # if self.locale_id is None:
        #    self.locale = self.get_default_locale()

        super().full_clean(*args, **kwargs)

    def clean(self):
        super().clean()
        # if not Page._slug_is_available(self.slug, self.get_parent(), self):
        #    raise ValidationError({'slug': _("This slug is already in use")})

    # @transaction.atomic
    def save(self, clean=True, user=None, log_action=False, **kwargs):

        if clean:
            self.full_clean()

        result = super().save(**kwargs)

        is_new = self.id is None

        if is_new:
            cls = type(self)
            logger.info(
                "Media item created: \"%s\" id=%d content_type=%s.%s",
                self.title,
                self.id,
                cls._meta.app_label,
                cls.__name__
            )

        if log_action is not None:

            if is_new:
                log(
                    instance=self,
                    action='wagtail.create',
                    user=user,
                    content_changed=True,
                )
            elif log_action:
                log(
                    instance=self,
                    action=log_action,
                    user=user
                )

        return result

    @staticmethod
    def will_be_deleted(instance, **kwargs):
        _ = instance.path
        pass

    @staticmethod
    def was_deleted(instance, **kwargs):

        try:
            instance.delete_storage_tree_at(default_storage, instance.path)
        except NotImplementedError:
            pass

        pass

    # noinspection SpellCheckingInspection
    def unpublish(self, set_expired=False, commit=True, user=None, log_action=True):
        """
        Unpublish the media_item by setting ``live`` to ``False``. Does nothing if ``live`` is already ``False``
        :param log_action: flag for logging the action. Pass False to skip logging. Can be passed an action string.
        Defaults to 'wagtail.unpublish'
        """
        if self.live:
            self.live = False
            self.has_unpublished_changes = True
            self.live_revision = None

            if set_expired:
                self.expired = True

            if commit:
                # using clean=False to bypass validation
                self.save(clean=False)

            # page_unpublished.send(sender=self.specific_class, instance=self.specific)

            if log_action:
                MediaItemLogEntry.objects.log_action(
                    instance=self,
                    action=log_action if isinstance(log_action, str) else 'wagtail.unpublish',
                    user=user,
                )

            logger.info("Media item unpublished: \"%s\" id=%d", self.title, self.id)

    @classmethod
    def get_indexed_objects(cls):
        content_type = ContentType.objects.get_for_model(cls)
        return super(MediaItem, cls).get_indexed_objects().filter(content_type=content_type)

    def get_indexed_instance(self):
        # This is accessed on save by the wagtailsearch signal handler, and in edge
        # cases (e.g. loading test fixtures), may be called before the specific instance's
        # entry has been created. In those cases, we aren't ready to be indexed yet, so
        # return None.
        try:
            return self.specific
        except self.specific_class.DoesNotExist:
            return None

    @classmethod
    def get_verbose_name(cls):
        """
        Returns the human-readable "verbose name" of this media_item model e.g "Blog media_item".
        """
        # This is similar to doing cls._meta.verbose_name.title()
        # except this doesn't convert any characters to lowercase
        return capfirst(cls._meta.verbose_name)

    @property
    def status_string(self):
        if not self.live:
            if self.expired:
                return _("expired")
            else:
                return _("not live")
        else:
            return _("live")

    def permissions_for_user(self, user):
        """
        Return a PagePermissionsTester object defining what actions the user can perform on this media_item
        """

        from media_catalogue.models import UserMediaItemPermissionsProxy

        user_perms = UserMediaItemPermissionsProxy(user)
        return user_perms.for_media_item(self)

    def get_view_restrictions(self):

        """
        Return a query set of all media_item view restrictions that apply to this media_item.

        This checks the current media_item for media item view restrictions.
        """

        media_item_ids_to_check = set()

        def add_media_item_to_check_list(media_item):
            # If the media_item is an alias, add the source media_item to the check list instead
            media_item_ids_to_check.add(media_item.id)

        # Check current media_item for view restrictions
        add_media_item_to_check_list(self)

        # noinspection PyUnresolvedReferences
        return MediaItemViewRestriction.objects.filter(media_item_id__in=media_item_ids_to_check)

    @property
    def edit_url(self):
        return reverse(APP_LABEL + ':edit', args=(quote(self.pk),))

    @property
    def delete_url(self):
        return reverse(APP_LABEL + ':delete', args=(quote(self.pk),))

    def render_in_responsive_cell(self, cell, template_context=None):
        return ''

    class Meta:
        verbose_name = _('Media Item')
        verbose_name_plural = _('Media Items')


MediaItemAttachment = create_model_attachment_class(MediaItem)


class UploadedMediaItem(models.Model):

    """
    Temporary storage for images uploaded through the multiple image uploader, when validation rules (e.g.
    required metadata fields) prevent creating an Image object from the image file alone. In this case,
    the media item file is stored against this model, to be turned into an media item object
    once the full form has been filled in.
    """

    file = MediaItemField(upload_to='uploaded_media_items', max_length=200)
    uploaded_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('uploaded by user'),
        null=True, blank=True, editable=False, on_delete=models.SET_NULL
    )
