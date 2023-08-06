
from wagtail import blocks
from wagtail_content_block.annotations import *

from aldine.blocks import BaseContentLayoutBlock

from .apps import get_app_label
from .adapters.adapter import get_media_catalogue_adapter

__all__ = ['MediaItemLayoutBlock']

APP_LABEL = get_app_label()


class MediaItemLayoutBlock(BaseContentLayoutBlock):

    class Meta:

        supported_item_types = [APP_LABEL + ".mediaitem", APP_LABEL + ".universalmediaitem"]

        responsive_delegate_var = "responsive_delegate"
        responsive_delegate = get_media_catalogue_adapter()

        annotations = ContentAnnotations(groups=[
            ContentAnnotationGroup(
                identifier='caption',
                label='Caption',
                fields=[
                    TextAreaAnnotationField(
                        identifier='text',
                        label='',
                        instance_value_path='content_object.title',
                        attributes={
                            'placeholder': 'Enter caption'
                        }
                    ),

                    TextAnnotationField(
                        identifier='anchor_identifier',
                        label='Anchor Identifier',
                        attributes={
                            'placeholder': ''
                        }
                    )
                ]
            ),

            ContentAnnotationGroup(
                identifier='link',
                label='Link',
                fields=[

                    PageChooserAnnotationField(
                        identifier='page',
                        label='Page',
                        attributes={
                        }
                    ),

                    TextAnnotationField(
                        identifier='page_fragment',
                        label='Page Fragment',
                        attributes={
                            'placeholder': ''
                        }
                    ),

                    TextAnnotationField(
                        identifier='external_url',
                        label='External URL',
                        attributes={
                            'placeholder': ''
                        }
                    )
                ]
            )
        ])

    def get_context(self, value, parent_context=None):

        context = super().get_context(value, parent_context)  # noqa
        context[self.meta.responsive_delegate_var] = self.meta.responsive_delegate

        return context

    def deconstruct(self):
        return blocks.Block.deconstruct(self)
