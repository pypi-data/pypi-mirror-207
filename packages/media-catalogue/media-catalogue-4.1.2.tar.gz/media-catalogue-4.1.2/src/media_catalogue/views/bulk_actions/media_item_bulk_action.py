
from abc import ABCMeta
from wagtail.admin.views.bulk_action import BulkAction

from media_catalogue.adapters.adapter import get_media_catalogue_adapter
from media_catalogue.adapters.registry import adapter_registry
from media_catalogue.apps import get_app_label


__all__ = ['MediaItemBulkAction']


APP_LABEL = get_app_label()


class ModelsDescriptor:

    def __init__(self):
        self.models = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, cls=None):
        if instance is None:
            return self

        if self.models is None:
            self.models = [adapter.model for adapter in adapter_registry.adapters]

        return self.models


class ModelsIterable:

    def __iter__(self):

        from media_catalogue.models.universal_media_items import UniversalMediaItem

        return iter([UniversalMediaItem] + [adapter.model for adapter in adapter_registry.adapters])


class MediaItemBulkActionMeta(ABCMeta):

    def __new__(mcls, name, bases, attrs, **kwargs):
        cls = super().__new__(mcls, name, bases, attrs, **kwargs)
        return cls


class MediaItemBulkAction(BulkAction):

    models = ModelsIterable()

    # models = ModelsDescriptor()

    """

    extras = dict()
    action_priority = 100
    models = []
    classes = set() CSS classes

    form_class = forms.Form
    cleaned_form = None

    """




    @property
    def display_name(self):
        return "{} action".format(self.adapter.get_verbose_name())

    def __init__(self, request, model):

        self.adapter = get_media_catalogue_adapter()
        # self.models = [self.adapter.model]
        self.permission_policy = self.adapter.permission_policy

        super().__init__(request, model)

    def get_queryset(self, model, object_ids):

        instances = self.adapter.model.objects.all()

        if object_ids is not None:
            instances = instances.filter(pk__in=object_ids)

        return instances
        # return get_list_or_404(self.adapter.model, pk__in=object_ids)

    def get_all_objects_in_listing_query(self, parent_id):

        listing_objects = self.get_queryset(self.model, None)

        # if parent_id is not None:
        #    listing_objects = listing_objects.filter(collection_id=parent_id)

        listing_objects = listing_objects.values_list('pk', flat=True)

        if 'q' in self.request.GET:
            query_string = self.request.GET.get('q', '')
            listing_objects = listing_objects.search(query_string).results()

        return listing_objects

    def get_execution_context(self):
        return {'action': self}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'adapter': self.adapter,
        })

        context['items_with_no_access'] = [
            {
                'item': media_item,
                'can_edit': self.permission_policy.user_has_permission_for_instance(self.request.user, 'change', media_item)
            } for media_item in context['items_with_no_access']
        ]
        return context
