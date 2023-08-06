from media_catalogue.models.errors import SourceMediaItemIOError


def get_rendition_or_not_found(media_item, specs):
    """
    Tries to get / create the rendition for the image or renders a not-found image if it does not exist.

    :param media_item: AbstractMediaItem
    :param specs: str or Filter
    :return: Rendition
    """
    try:
        return media_item.get_rendition(specs)
    except SourceMediaItemIOError:
        # Image file is (probably) missing from /media/original_images - generate a dummy
        # rendition so that we just output a broken image, rather than crashing out completely
        # during rendering.
        Rendition = media_item.renditions.model  # pick up any custom MediaItem / Rendition classes that may be in use
        rendition = Rendition(image=media_item, width=0, height=0)
        rendition.file.name = 'not-found'
        return rendition
