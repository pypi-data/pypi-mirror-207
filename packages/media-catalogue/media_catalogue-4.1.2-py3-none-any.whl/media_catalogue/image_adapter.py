
from wagtail.images.permissions import permission_policy as image_permission_policy
from wagtail.images import get_image_model

from aldine.images import render_image_in_responsive_cell, ImageCurator

from .adapters.adapter import MediaCatalogueAdapter

__all__ = ['ImageAdapter']


class ImageAdapter(MediaCatalogueAdapter):

    def __init__(self):

        model = get_image_model()
        add_url_specifiers = [('wagtailimages:add_multiple', (), model)] # noqa

        super().__init__(model=model,
                         permission_policy=image_permission_policy,
                         add_url_specifiers=add_url_specifiers)

        self.browser_add_url_specifier = 'wagtailimages:add_multiple'
        self.browser_add_prompt = 'Add an image'
        self.browser_edit_url_specifier = 'wagtailimages:edit'
        self.browser_delete_url_specifier = 'wagtailimages:delete'
        self.browser_bulk_action_type = 'IMAGE'
        self.browser_get_key_for_instance = None

        self.curator = ImageCurator()

    # noinspection PyMethodMayBeStatic
    def title_for(self, instance):
        return instance.title

    # noinspection PyMethodMayBeStatic
    def content_url_for(self, instance, file_name):
        rendition = instance.get_rendition('original')
        return rendition.url

    # noinspection PyMethodMayBeStatic
    def content_path_for(self, instance, file_name):
        return None

    # noinspection PyMethodMayBeStatic
    def create_panel_for(self, instance, request):
        return None

    # noinspection PyMethodMayBeStatic
    def delete_instance(self, instance):
        instance.delete()

    # noinspection PyMethodMayBeStatic
    def bulk_delete_instances(self, instances):
        for instance in instances:
            instance.delete()

    def render_in_responsive_cell(self, item, cell, template_context=None):

        if item is None:
            return ''

        attributes = {
            "loading": "lazy"
        }

        return render_image_in_responsive_cell(item, cell, self.curator, attributes=attributes)

    def render_preview_inner(self, instance, **kwargs):

        rendition = instance.get_rendition('max-165x165')
        preview_html = rendition.__html__()

        return '<div class="fit-content">{}</div>'.format(preview_html)
