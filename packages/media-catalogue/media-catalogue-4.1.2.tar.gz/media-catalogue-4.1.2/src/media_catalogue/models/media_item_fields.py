

from django.core.files import File
from django.core import checks

from django.db.models import signals, FileField
from django.db.models.fields.files import FieldFile, FileDescriptor

from django.utils.translation import gettext_lazy as _

from ..form_fields import BaseMediaItemField


class MediaItemFile(File):
    """
    A mixin for use alongside django.core.files.base.File, which provides
    additional features for dealing with images.
    """

    @property
    def width(self):
        return self._get_media_item_dimensions()[0]

    @property
    def height(self):
        return self._get_media_item_dimensions()[1]

    def _get_media_item_dimensions(self):
        if not hasattr(self, "_dimensions_cache"):
            close = self.closed
            self.open()
            self._dimensions_cache = get_media_item_dimensions(self, close=close)
        return self._dimensions_cache


def get_media_item_dimensions(file_or_path, close=False):
    """
    Return the (width, height) of an image, given an open file or a path.  Set
    'close' to True to close the file at the end if it is initially in an open
    state.
    """

    """
    from PIL import ImageFile as PillowImageFile

    p = PillowImageFile.Parser()
    if hasattr(file_or_path, "read"):
        file = file_or_path
        file_pos = file.tell()
        file.seek(0)
    else:
        try:
            file = open(file_or_path, "rb")
        except OSError:
            return (None, None)
        close = True
    try:
        # Most of the time Pillow only needs a small chunk to parse the image
        # and get the dimensions, but with some TIFF files Pillow needs to
        # parse the whole file.
        chunk_size = 1024
        while 1:
            data = file.read(chunk_size)
            if not data:
                break
            try:
                p.feed(data)
            except zlib.error as e:
                # ignore zlib complaining on truncated stream, just feed more
                # data to parser (ticket #19457).
                if e.args[0].startswith("Error -5"):
                    pass
                else:
                    raise
            except struct.error:
                # Ignore PIL failing on a too short buffer when reads return
                # less bytes than expected. Skip and feed more data to the
                # parser (ticket #24544).
                pass
            except RuntimeError:
                # e.g. "RuntimeError: could not create decoder object" for
                # WebP files. A different chunk_size may work.
                pass
            if p.image:
                return p.image.size
            chunk_size *= 2
        return (None, None)
    finally:
        if close:
            file.close()
        else:
            file.seek(file_pos)
    """

    return None, None


class MediaItemFileDescriptor(FileDescriptor):
    """
    Just like the FileDescriptor, but for MediaItemFields. The only difference is
    assigning the width/height to the width_field/height_field, if appropriate.
    """

    def __set__(self, instance, value):
        previous_file = instance.__dict__.get(self.field.attname)
        super().__set__(instance, value)

        # To prevent recalculating image dimensions when we are instantiating
        # an object from the database (bug #11084), only update dimensions if
        # the field had a value before this assignment.  Since the default
        # value for FileField subclasses is an instance of field.attr_class,
        # previous_file will only be None when we are called from
        # Model.__init__().  The ImageField.update_dimension_fields method
        # hooked up to the post_init signal handles the Model.__init__() cases.
        # Assignment happening outside of Model.__init__() will trigger the
        # update right here.
        if previous_file is not None:
            self.field.update_dimension_fields(instance, force=True)


class MediaItemFieldFile(MediaItemFile, FieldFile):
    def delete(self, save=True):
        # Clear the image dimensions cache
        if hasattr(self, "_dimensions_cache"):
            del self._dimensions_cache
        super().delete(save)


class MediaItemField(FileField):
    attr_class = MediaItemFieldFile
    descriptor_class = MediaItemFileDescriptor
    description = _("Media Item")

    def __init__(
            self,
            verbose_name=None,
            name=None,
            width_field=None,
            height_field=None,
            **kwargs,
    ):
        self.width_field, self.height_field = width_field, height_field
        super().__init__(verbose_name, name, **kwargs)

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_image_library_installed(),
        ]

    def _check_image_library_installed(self):
        try:
            from PIL import Image  # NOQA
        except ImportError:
            return [
                checks.Error(
                    "Cannot use MediaItemField because Pillow is not installed.",
                    hint=(
                        "Get Pillow at https://pypi.org/project/Pillow/ "
                        'or run command "python -m pip install Pillow".'
                    ),
                    obj=self,
                    id="fields.E210",
                )
            ]
        else:
            return []

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.width_field:
            kwargs["width_field"] = self.width_field
        if self.height_field:
            kwargs["height_field"] = self.height_field
        return name, path, args, kwargs

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)
        # Attach update_dimension_fields so that dimension fields declared
        # after their corresponding image field don't stay cleared by
        # Model.__init__, see bug #11196.
        # Only run post-initialization dimension update on non-abstract models
        if not cls._meta.abstract:
            signals.post_init.connect(self.update_dimension_fields, sender=cls)

    def update_dimension_fields(self, instance, force=False, *args, **kwargs):
        """
        Update field's width and height fields, if defined.

        This method is hooked up to model's post_init signal to update
        dimensions after instantiating a model instance.  However, dimensions
        won't be updated if the dimensions fields are already populated.  This
        avoids unnecessary recalculation when loading an object from the
        database.

        Dimensions can be forced to update with force=True, which is how
        MediaItemFileDescriptor.__set__ calls this method.
        """
        # Nothing to update if the field doesn't have dimension fields or if
        # the field is deferred.
        has_dimension_fields = self.width_field or self.height_field
        if not has_dimension_fields or self.attname not in instance.__dict__:
            return

        # getattr will call the MediaItemFileDescriptor's __get__ method, which
        # coerces the assigned value into an instance of self.attr_class
        # (ImageFieldFile in this case).
        file = getattr(instance, self.attname)

        # Nothing to update if we have no file and not being forced to update.
        if not file and not force:
            return

        dimension_fields_filled = not (
                (self.width_field and not getattr(instance, self.width_field))
                or (self.height_field and not getattr(instance, self.height_field))
        )
        # When both dimension fields have values, we are most likely loading
        # data from the database or updating an image field that already had
        # an image stored.  In the first case, we don't want to update the
        # dimension fields because we are already getting their values from the
        # database.  In the second case, we do want to update the dimensions
        # fields and will skip this return because force will be True since we
        # were called from MediaItemFileDescriptor.__set__.
        if dimension_fields_filled and not force:
            return

        # file should be an instance of ImageFieldFile or should be None.
        if file:
            width = file.width
            height = file.height
        else:
            # No file, so clear dimensions fields.
            width = None
            height = None

        # Update the width and height fields.
        if self.width_field:
            setattr(instance, self.width_field, width)
        if self.height_field:
            setattr(instance, self.height_field, height)

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": BaseMediaItemField,
                **kwargs,
            }
        )

