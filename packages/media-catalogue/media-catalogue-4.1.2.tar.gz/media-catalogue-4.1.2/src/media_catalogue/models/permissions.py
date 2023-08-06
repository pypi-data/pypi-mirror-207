# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from wagtail.permission_policies.collections import CollectionOwnershipPermissionPolicy
from .media_items import MediaItem

__all__ = ['permission_policy', 'GroupMediaItemPermission', 'UserMediaItemPermissionsProxy']

permission_policy = CollectionOwnershipPermissionPolicy(
    MediaItem,
    auth_model=MediaItem,
    owner_field_name='created_by_user'
)


MEDIA_ITEM_PERMISSION_TYPES = [
    ('add', _("Add"), _("Add/edit media items you own")),
    ('edit', _("Edit"), _("Edit any media item")),
    ('publish', _("Publish"), _("Publish any media item")),
    ('lock', _("Lock"), _("Lock/unlock media items you've locked")),
    ('unlock', _("Unlock"), _("Unlock any media item")),
]

MEDIA_ITEM_PERMISSION_TYPE_CHOICES = [
    (identifier, long_label)
    for identifier, short_label, long_label in MEDIA_ITEM_PERMISSION_TYPES
]


class GroupMediaItemPermission(models.Model):

    group = models.ForeignKey(Group, verbose_name=_('group'), related_name='media_item_permissions', on_delete=models.CASCADE)
    media_item = models.ForeignKey('MediaItem', verbose_name=_('media_item'), related_name='group_permissions', on_delete=models.CASCADE)

    permission_type = models.CharField(
        verbose_name=_('permission type'),
        max_length=20,
        choices=MEDIA_ITEM_PERMISSION_TYPE_CHOICES
    )

    class Meta:
        unique_together = ('group', 'media_item', 'permission_type')
        verbose_name = _('Group Media Item Permission')
        verbose_name_plural = _('Group Media Item Permissions')

    def __str__(self):
        return "Group %d ('%s') has permission '%s' on media_item %d ('%s')" % (
            self.group.id, self.group,
            self.permission_type,
            self.media_item.id, self.media_item
        )


class UserMediaItemPermissionsProxy:
    """Helper object that encapsulates all the media item permission rules that this user has."""

    def __init__(self, user):
        self.user = user

        if user.is_active and not user.is_superuser:
            self.permissions = GroupMediaItemPermission.objects.filter(group__user=self.user).select_related('media_item')

    def for_media_item(self, media_item):
        """Return a MediaItemPermissionTester object that can be used to query whether this user has
        permission to perform specific tasks on the given media item"""
        return MediaItemPermissionTester(self, media_item)

    def explorable_media_items(self):
        """Return a queryset of media items that the user has access to view in the
        explorer (e.g. add/edit/publish permission). Includes all media items with
        specific group permissions."""
        # Deal with the trivial cases first...
        if not self.user.is_active:
            return MediaItem.objects.none()
        if self.user.is_superuser:
            return MediaItem.objects.all()

        result = MediaItem.objects.none()

        # Creates a union queryset of all objects the user has access to add,
        # edit and publish
        for perm in self.permissions.filter(
            Q(permission_type="add")
            | Q(permission_type="edit")
            | Q(permission_type="publish")
            | Q(permission_type="lock")
        ):
            result |= MediaItem.objects.filter(Q(id=perm.media_item.id))

        return result

    def editable_media_items(self):
        """Return a queryset of the media items that this user has permission to edit"""
        # Deal with the trivial cases first...
        if not self.user.is_active:
            return MediaItem.objects.none()
        if self.user.is_superuser:
            return MediaItem.objects.all()

        editable_media_items = MediaItem.objects.none()

        for perm in self.permissions.filter(permission_type='add'):
            editable_media_items |= MediaItem.objects.filter(Q(id=perm.media_item.id, owner=self.user))

        for perm in self.permissions.filter(permission_type='edit'):
            editable_media_items |= MediaItem.objects.filter(Q(id=perm.media_item.id, owner=self.user))

        return editable_media_items

    def can_edit_media_items(self):
        """Return True if the user has permission to edit any media items."""
        return self.editable_media_items().exists()

    def publishable_media_items(self):
        """Return a queryset of the media items that this user has permission to publish"""
        # Deal with the trivial cases first...
        if not self.user.is_active:
            return MediaItem.objects.none()
        if self.user.is_superuser:
            return MediaItem.objects.all()

        result = MediaItem.objects.none()

        for perm in self.permissions.filter(permission_type='publish'):
            result |= MediaItem.objects.filter(Q(id=perm.media_item.id))

        return result

    def can_publish_media_items(self):
        """Return True if the user has permission to publish any media items."""
        return self.publishable_media_items().exists()


class MediaItemPermissionTester:
    def __init__(self, user_perms, media_item):
        self.user = user_perms.user
        self.user_perms = user_perms
        self.media_item = media_item

        if self.user.is_active and not self.user.is_superuser:
            self.permissions = set(
                perm.permission_type for perm in user_perms.permissions
            )

    def can_edit(self):
        if not self.user.is_active:
            return False

        if self.user.is_superuser:
            return True

        if 'edit' in self.permissions:
            return True

        if 'add' in self.permissions and self.media_item.uploaded_by_user_id == self.user.pk:
            return True

        # if self.media_item.current_workflow_task:
        #    if self.media_item.current_workflow_task.user_can_access_editor(self.media_item, self.user):
        #        return True

        return False

    def can_delete(self):
        if not self.user.is_active:
            return False

        if self.user.is_superuser:
            # superusers require no further checks
            return True

        if 'edit' in self.permissions:
            return True

        elif 'add' in self.permissions:
            media_items_to_delete = MediaItem.objects.filter(Q(id=self.media_item.id))

            if 'publish' in self.permissions:
                # we don't care about live state, but all media items must be owned by this user
                # (i.e. eliminating media items owned by this user must give us the empty set)
                return not media_items_to_delete.exclude(created_by_user=self.user).exists()
            else:
                # all media items must be owned by this user and non-live
                # (i.e. eliminating non-live media items owned by this user must give us the empty set)
                return not media_items_to_delete.exclude(live=False, created_by_user=self.user).exists()

        else:
            return False

    # noinspection SpellCheckingInspection
    def can_unpublish(self):
        if not self.user.is_active:
            return False
        if not self.media_item.live:
            return False

        return self.user.is_superuser or ('publish' in self.permissions)

    def can_publish(self):
        if not self.user.is_active:
            return False

        return self.user.is_superuser or ('publish' in self.permissions)

    def can_set_view_restrictions(self):
        return self.can_publish()


