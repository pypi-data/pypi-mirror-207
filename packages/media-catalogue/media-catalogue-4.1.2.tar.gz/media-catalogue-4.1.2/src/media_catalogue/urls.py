from django.urls import re_path

from .adapters.adapter import get_media_catalogue_adapter
from .apps import get_app_label

app_name = get_app_label()

urlpatterns = get_media_catalogue_adapter().create_urls() + [
]
