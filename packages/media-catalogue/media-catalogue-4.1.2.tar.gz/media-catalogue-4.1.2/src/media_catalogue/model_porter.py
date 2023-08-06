import os

from django.conf import settings

from wagtail_content_admin.frontend import pack_content_item_specifier

from wagtail_attachments.models.attachment_roles import AttachmentRole
from wagtail_attachments.models.attachment_fields import ContentAttachmentFile

from model_porter.config import ModelPorterConfig
from model_porter.repository import file_reader_from_path


from .models import MediaItemAttachment
from .blocks import MediaItemChooserBlock
from .adapters.adapter import generalize


def build_media_attachment(*, specifier, context, role_identifier):

    role = AttachmentRole.objects.get(identifier=role_identifier)
    instance = context.get_variable(context.INSTANCE_VARIABLE)
    template = None

    if not isinstance(specifier, str):
        specifier, template = specifier

    reader = file_reader_from_path(specifier, context)
    data = reader.read()
    file = ContentAttachmentFile(data, name=os.path.basename(specifier))

    attachment = MediaItemAttachment()
    attachment.model = instance
    attachment.role_id = role.id
    attachment.file = file

    return [attachment]


def build_media_attachments(*, specifiers, context, role_identifier):

    result = []

    for specifier in specifiers:
        result.extend(build_media_attachment(specifier=specifier, context=context, role_identifier=role_identifier))

    return result


def media_chooser_value(*, items, context):

    result = []

    for item in items:

        if isinstance(item, tuple) or isinstance(item, list):
            identifier, annotations = item
        else:
            identifier = item
            annotations = None

        instance = context.get_instance(identifier, None)
        instance = generalize(instance)

        result.append(pack_content_item_specifier(instance, annotations))

    result = {
        MediaItemChooserBlock.TYPE_FIELD_NAME: MediaItemChooserBlock._meta_class.chooser_block_name, # noqa
        MediaItemChooserBlock._meta_class.chooser_block_name: result # noqa
    }

    return result


def finalise_media_item(*, instance, context):

    if not settings.MEDIA_CATALOGUE_UNIFY_MEDIA:
        return instance

    instance.save()
    instance = generalize(instance)

    return instance


class MediaCatalogueConfig(ModelPorterConfig):

    def __init__(self, app_label, module):
        super(MediaCatalogueConfig, self).__init__(app_label, module)
        self.register_function_action(media_chooser_value, context_argument='context')
        self.register_function_action(finalise_media_item, context_argument='context')
        self.register_function_action(build_media_attachment, context_argument='context')
        self.register_function_action(build_media_attachments, context_argument='context')
