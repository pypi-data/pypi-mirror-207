from django.conf import settings

__all__ = ['unify_media', 'hide_images_in_admin_menu']


def unify_media():
    """
    Indicates whether the media catalogue includes models which have a media catalogue adapter registered (such as images)
    or just models deriving from MediaItem.
    """

    return settings.MEDIA_CATALOGUE_UNIFY_MEDIA


def hide_images_in_admin_menu():
    """
    Indicates whether the media catalogue hides the image menu entry in the admin interface.
    """

    return settings.MEDIA_CATALOGUE_HIDE_IMAGES_IN_ADMIN_MENU
