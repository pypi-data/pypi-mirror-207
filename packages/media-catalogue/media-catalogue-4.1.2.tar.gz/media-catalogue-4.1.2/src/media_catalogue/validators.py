
from django.core.validators import FileExtensionValidator, get_available_image_extensions

__all__ = ['validate_media_file_extension']


def get_available_media_extensions():

    result = list(get_available_image_extensions())
    return result


def validate_media_file_extension(value):
    return FileExtensionValidator(allowed_extensions=get_available_media_extensions())(
        value
    )
