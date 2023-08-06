from django.urls import path

from .apps import get_app_label
from .views import add, usage, history
from .views.multiple import create_multiple, delete_upload_multiple, edit_multiple
from .adapters.adapter import get_media_catalogue_adapter

app_name = get_app_label()

urlpatterns = get_media_catalogue_adapter().create_admin_urls() + [

    # path('choose/upload/', chooser.chooser_upload, name='chooser_upload'),
    # path('choose/select_layout/<str:media_item_pk>/', chooser.chooser_select_layout, name='chooser_select_layout'),

    path('add/<slug:app_label>/<slug:model_name>/', add.add, name='add'),
    # path('multiple/add/<slug:app_label>/<slug:model_name>/', add_multiple.AddView.as_view(), name='add_multiple'),

    path('add/', add.media_type_selection, name='add_media_type_selection'),
    # path('multiple/add/', lambda request: add.media_type_selection(request, add_multiple=True), name='add_multiple_media_type_selection'),
    path('multiple/add/', lambda request: add.media_type_selection(request, add_multiple=False), name='add_multiple_media_type_selection'),

    # path('edit/multiple/<str:media_item_pk>/', edit_multiple.EditView.as_view(), name='edit_multiple'),
    path('create_from_uploaded_image/multiple/<str:uploaded_media_item_pk>/',
         create_multiple.CreateFromUploadedMediaItemView.as_view(), name='create_multiple_from_uploaded_media_item'),

    # path('delete/multiple/', delete.delete, name='delete_multiple'),

    path('delete_upload/multiple/', delete_upload_multiple.DeleteUploadView.as_view(),
         name='delete_upload_multiple'),

    # path('edit/<str:media_item_pk>/', editor.Editor().as_view(), name='edit'),
    # path('delete/<str:media_item_pk>/', delete.delete, name='delete'),
    path('usage/<str:media_item_pk>/', usage.usage, name='usage'),
    path('history/<str:media_item_pk>/', history.HistoryView.as_view(), name='history'),

]
