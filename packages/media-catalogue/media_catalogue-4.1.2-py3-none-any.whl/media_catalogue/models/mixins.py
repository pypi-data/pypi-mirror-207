# -*- coding: utf-8 -*-

import os

from django.db.models import DEFERRED
from django.core.files.storage import default_storage as DEFAULT_STORAGE # noqa
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe

from django.contrib.contenttypes.models import ContentType

from PIL import Image as PILImage

from ..apps import get_app_label

__all__ = ['ChangeScope', 'ChangeScopeMixin', 'SpecificMixin', 'StorageMixin', 'PreviewGeneratorMixin']


APP_LABEL = get_app_label()


class ChangeScope(object):

    def __init__(self, media_item):
        self.media_item = media_item

    def __enter__(self):

        self.media_item.change_level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.media_item.change_level -= 1

        if self.media_item.change_count != 0 and self.media_item.change_level == 0:
            self.media_item.change_count = 0
            self.media_item.assemble()


class ChangeScopeMixin:

    class Meta:
        abstract = True

    @property
    def change_level(self):
        return self.change_level_

    @change_level.setter
    def change_level(self, value):
        self.change_level_ = value

    @property
    def change_count(self):
        return self.change_count_

    @change_count.setter
    def change_count(self, value):
        self.change_count_ = value

    @property
    def change_scope(self):
        return ChangeScope(self)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.change_level_ = 0
        self.change_count_ = 0

    def did_change(self):

        if self.change_level_ == 0:
            self.change_count_ = 0
            self.assemble()
        else:
            self.change_count_ += 1

    def assemble(self):
        pass


class SpecificMixin:

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def cached_content_type(self):
        """
        .. versionadded:: 2.10

        Return this media_item's ``content_type`` value from the ``ContentType``
        model's cached manager, which will avoid a database query if the
        object is already in memory.
        """
        return ContentType.objects.get_for_id(
                self.content_type_id)  # noqa

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
        return self.cached_content_type.model_class()

    @cached_property
    def specific(self):
        """
        Returns this media_item in its most specific subclassed form with all field
        values fetched from the database. The result is cached in memory.
        """
        return self.get_specific()

    @cached_property
    def specific_deferred(self):
        """
        .. versionadded:: 2.12

        Returns this media_item in its most specific subclassed form without any
        additional field values being fetched from the database. The result
        is cached in memory.
        """
        return self.get_specific(deferred=True)

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
        been removed from the codebase, a generic ``Page`` object will be
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
            return self

        if isinstance(self, model_class):
            # self is already the an instance of the most specific class
            return self

        if deferred:
            # Generate a tuple of values in the order expected by __init__(),
            # with missing values substituted with DEFERRED ()
            values = tuple(
                getattr(self, f.attname, self.pk if f.primary_key else DEFERRED)  # noqa
                for f in model_class._meta.concrete_fields
            )
            # Create object from known attribute values
            specific_obj = model_class(*values)
            specific_obj._state.adding = self._state.adding  # noqa
        else:
            # Fetch object from database
            specific_obj = model_class._default_manager.get(id=self.id)  # noqa

        # Copy additional attribute values
        for attr in copy_attrs or ():
            if attr in self.__dict__:
                setattr(specific_obj, attr, getattr(self, attr))

        return specific_obj


class StorageMixin:

    class Meta:
        abstract = True

    storage_root = APP_LABEL

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_ = None

    @property
    def path(self):
        if self.path_ is None:
            self.path_ = self.build_path_()

        return self.path_

    # noinspection PyMethodMayBeStatic
    def is_stored_locally(self):
        return False

    def build_path_(self):

        # media_catalogue/<app_label>.<model_name>/<username>/<year>-<month>-<day>/

        # self.specific._meta.app_label,  # noqa
        # self.specific._meta.model_name,  # noqa
        # creation_date = self.created_at  # noqa
        # creation_date_path = "{:04d}-{:02d}-{:02d}".format(creation_date.year, creation_date.month, creation_date.day)
        # user_name = self.created_by_user.get_username()  # noqa

        path = os.path.join(self.storage_root, '{:d}'.format(self.id)) # noqa
        return path

    @cached_property
    def local_attachments_path(self):
        return 'attachments/'

    @cached_property
    def attachments_path(self):
        return os.path.join(self.path, self.local_attachments_path)

    def delete_attachments(self):

        try:
            self.delete_storage_tree_at(DEFAULT_STORAGE, self.attachments_path)
        except NotImplementedError:
            pass

    @cached_property
    def local_content_path(self):
        return 'content/'

    @cached_property
    def content_path(self):
        return os.path.join(self.path, self.local_content_path)

    def content_url_for(self, name):
        return DEFAULT_STORAGE.url(os.path.join(self.content_path, name))

    def delete_content(self):

        try:
            if self.created_at is not None:  # noqa
                self.delete_storage_tree_at(DEFAULT_STORAGE, self.content_path)
        except NotImplementedError:
            pass

    @staticmethod
    def delete_storage_tree_at(storage, path):

        try:
            root_directories, root_files = storage.listdir(path)
        except FileNotFoundError:
            return

        stack = [(root_directories, root_files, 0, path)]

        while stack:

            directories, files, index, root_path = stack[-1]  # noqa

            if index < len(directories):

                stack[-1] = directories, files, index + 1, root_path

                root_path = os.path.join(root_path, directories[index])

                try:
                    nested_directories, nested_files = storage.listdir(root_path)
                    stack.append((nested_directories, nested_files, 0, root_path))
                except FileNotFoundError:
                    pass

                continue

            for file in files:
                file_path = os.path.join(root_path, file)

                try:
                    storage.delete(file_path)
                except FileNotFoundError:
                    pass

            for directory in directories:
                directory_path = os.path.join(root_path, directory)
                storage.delete(directory_path)

            stack.pop()

        storage.delete(path)


class PreviewGeneratorMixin:

    class Meta:
        abstract = True

    @property
    def preview_image_path(self):
        return os.path.join(self.path, 'preview.png')

    @property
    def preview_image_url(self):
        return DEFAULT_STORAGE.url(self.preview_image_path)

    @property
    def has_preview_image(self):

        image_path = DEFAULT_STORAGE.path(self.preview_image_path)

        try:
            with PILImage.open(image_path):
                return True

        except FileNotFoundError:
            return False

    def generate_preview_image(self):
        dimensions = 165, 165

        with PILImage.new(mode="RGB", size=dimensions, color=(128, 128, 128)) as image:
            image_path = DEFAULT_STORAGE.path(self.preview_image_path)
            image.save(image_path, optimize=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render_preview_html(self):
        return mark_safe('<div class="media-item-preview"><img src="{}"/></div>'.format(self.preview_image_url))

    """
    def render_preview_image(self, filter=''):

        if isinstance(filter, str):
            filter = Filter(spec=filter)

        image = self.preview_image
        cache_key = filter.get_cache_key(image)
        generated_image = filter.run(image, BytesIO())

        return None
    """
