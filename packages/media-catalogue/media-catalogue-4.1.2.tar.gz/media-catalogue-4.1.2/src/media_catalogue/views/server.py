
from django.conf import settings
from django.core.files.storage import default_storage as DEFAULT_STORAGE
from django.core.exceptions import PermissionDenied
from django.contrib.admin.utils import quote, unquote

from django.http import Http404, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.views.generic.base import View

from wagtail.utils import sendfile_streaming_backend
from wagtail.utils.sendfile import sendfile

from ..adapters.adapter import get_media_catalogue_adapter
from ..apps import get_app_label
from django_auxiliaries.url_signature import verify_signed_url

__all__ = ['Server']

APP_LABEL = get_app_label()


class Server(View):

    adapter = None
    permissions = None
    signature_key = None
    url_specifier = APP_LABEL + "_frontend:serve"

    def __init__(self, adapter=None, permissions=None, **kwargs):
        super().__init__(**kwargs)

        if adapter is None:
            adapter = get_media_catalogue_adapter()

        if permissions is None:
            permissions = []

        self.adapter = adapter
        self.permissions = permissions

        result = self.get_inner

        # f = adapter.permission_checker.require_any(permissions)
        # result = f(result)

        self.get = result

    def get_inner(self, request, media_item_id, content_filename, signature=None):

        if not signature:
            raise PermissionDenied

        if not verify_signed_url(media_item_id, content_filename, url_specifier=self.url_specifier, signature=signature, key=self.signature_key):
            raise PermissionDenied

        components = content_filename.split('/')

        if len(components) != 1 or content_filename == "..":
            raise PermissionDenied

        # Get items (filtered by user permission)
        #instances = self.adapter.permission_policy.instances_user_has_any_permission_for(
        #    request.user, self.permissions
        #).order_by('-created_at')

        instances = self.adapter.permission_policy.model.objects.all().order_by('-created_at')
        instances = instances.filter(pk=int(media_item_id))

        if not instances:
            raise Http404()

        media_item = instances[0]

        content_url = self.adapter.content_url_for(media_item, content_filename)

        if content_url:
            return HttpResponseRedirect(content_url)  # Http404("Not found.")

        content_path = self.adapter.content_path_for(media_item, content_filename)

        if content_path is None:
            raise Http404("Not found.")

        try:
            local_path = DEFAULT_STORAGE.path(content_path)
        except NotImplementedError:
            local_path = None

        if local_path:

            # Use wagtail.utils.sendfile to serve the file;
            # this provides support for mimetypes, if-modified-since and django-sendfile backends

            backend = sendfile_streaming_backend.sendfile

            if hasattr(settings, 'SENDFILE_BACKEND'):
                backend = None  # instruct sendfile to use the backend defined in the settings

            return sendfile(
                request,
                local_path,
                attachment=True,
                attachment_filename=content_filename,
                backend=backend
            )

        else:
            raise Http404()
            # return HttpResponsePermanentRedirect(url)

