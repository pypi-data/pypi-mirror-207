from django.apps import apps
from django.http import Http404

from ..models.media_items import get_media_item_models

__all__ = ['get_media_item_model_from_url_params']


def get_media_item_model_from_url_params(app_name, model_name):

    """
    Retrieve a model from an app_label / model_name combo.
    Raise Http404 if the model is not a valid media item type.
    """

    try:
        model = apps.get_model(app_name, model_name)
    except LookupError:
        raise Http404

    if model not in get_media_item_models():
        raise Http404

    return model
