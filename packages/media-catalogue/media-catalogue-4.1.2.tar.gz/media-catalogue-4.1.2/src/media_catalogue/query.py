# -*- coding: utf-8 -*-

import warnings

from collections import defaultdict

from django.apps import apps
from django.db.models import Q, QuerySet
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import BaseIterable

from wagtail.search.queryset import SearchableQuerySetMixin

__all__ = ['MediaItemQuerySet']


class SpecificIterable(BaseIterable):
    def __iter__(self):
        return specific_iterator(self.queryset)


class DeferredSpecificIterable(BaseIterable):
    def __iter__(self):
        return specific_iterator(self.queryset, defer=True)


def specific_iterator(qs, defer=False):
    """
    This efficiently iterates all the specific media items in a queryset, using
    the minimum number of queries.

    This should be called from ``MediaItemQuerySet.specific``
    """

    from media_catalogue.models import MediaItem

    annotation_aliases = qs.query.annotations.keys()
    values = qs.values('pk', 'content_type', *annotation_aliases)

    annotations_by_pk = defaultdict(list)
    if annotation_aliases:
        # Extract annotation results keyed by pk so we can reapply to fetched media items.
        for data in values:
            annotations_by_pk[data['pk']] = {k: v for k, v in data.items() if k in annotation_aliases}

    pks_and_types = [[v['pk'], v['content_type']] for v in values]
    pks_by_type = defaultdict(list)
    for pk, content_type in pks_and_types:
        pks_by_type[content_type].append(pk)

    # Content types are cached by ID, so this will not run any queries.
    content_types = {pk: ContentType.objects.get_for_id(pk)
                     for _, pk in pks_and_types}

    # Get the specific instances of all media items, one model class at a time.
    media_items_by_type = {}
    missing_pks = []

    for content_type, pks in pks_by_type.items():
        # look up model class for this content type, falling back on the original
        # model (i.e. Page) if the more specific one is missing
        model = content_types[content_type].model_class() or qs.model
        media_items = model.objects.filter(pk__in=pks)

        if defer:
            # Defer all specific fields
            fields = [field.attname for field in MediaItem._meta.get_fields() if field.concrete]
            media_items = media_items.only(*fields)

        media_items_for_type = {page.pk: page for page in media_items}
        media_items_by_type[content_type] = media_items_for_type
        missing_pks.extend(
            pk for pk in pks if pk not in media_items_for_type
        )

    # Fetch generic media items to supplement missing items
    if missing_pks:
        generic_media_items = MediaItem.objects.filter(pk__in=missing_pks).select_related('content_type').in_bulk()
        warnings.warn(
            "Specific versions of the following media items could not be found. "
            "This is most likely because a database migration has removed "
            "the relevant table or record since the media_item was created:\n{}".format([
                {'id': p.id, 'title': p.title, 'type': p.content_type}
                for p in generic_media_items.values()
            ]), category=RuntimeWarning
        )
    else:
        generic_media_items = {}

    # Yield all media items in the order they occurred in the original query.
    for pk, content_type in pks_and_types:
        try:
            page = media_items_by_type[content_type][pk]
        except KeyError:
            page = generic_media_items[pk]
        if annotation_aliases:
            # Reapply annotations before returning
            for annotation, value in annotations_by_pk.get(page.pk, {}).items():
                setattr(page, annotation, value)
        yield page


class MediaItemQuerySet(SearchableQuerySetMixin, QuerySet):

    # noinspection PyMethodMayBeStatic
    def live_q(self):
        return Q(live=True)

    def live(self):
        """
        This filters the QuerySet to only contain published media items.
        """
        return self.filter(self.live_q())

    def not_live(self):
        """
        This filters the QuerySet to only contain unpublished media items.
        """
        return self.exclude(self.live_q())

    # noinspection PyMethodMayBeStatic
    def media_item_q(self, other):
        return Q(id=other.id)

    def media_item(self, other):
        """
        This filters the QuerySet so it only contains the specified media item.
        """
        return self.filter(self.media_item_q(other))

    def not_media_item(self, other):
        """
        This filters the QuerySet so it doesn't contain the specified media_item.
        """
        return self.exclude(self.media_item_q(other))

    # noinspection PyMethodMayBeStatic
    def type_q(self, klass):
        content_types = ContentType.objects.get_for_models(*[
            model for model in apps.get_models()
            if issubclass(model, klass)
        ]).values()

        return Q(content_type__in=list(content_types))

    def type(self, model):
        """
        This filters the QuerySet to only contain media item that are an instance
        of the specified model (including subclasses).
        """
        return self.filter(self.type_q(model))

    def not_type(self, model):
        """
        This filters the QuerySet to not contain any media items which are an instance of the specified model.
        """
        return self.exclude(self.type_q(model))

    # noinspection PyMethodMayBeStatic
    def exact_type_q(self, klass):
        return Q(content_type=ContentType.objects.get_for_model(klass))

    def exact_type(self, model):
        """
        This filters the QuerySet to only contain media items that are an instance of the specified model
        (matching the model exactly, not subclasses).
        """
        return self.filter(self.exact_type_q(model))

    def not_exact_type(self, model):
        """
        This filters the QuerySet to not contain any media items which are an instance of the specified model
        (matching the model exactly, not subclasses).
        """
        return self.exclude(self.exact_type_q(model))

    def specific(self, defer=False):
        """
        This efficiently gets all the specific media items for the queryset, using
        the minimum number of queries.

        When the "defer" keyword argument is set to True, only the basic media item
        fields will be loaded and all specific fields will be deferred. It
        will still generate a query for each media item type though (this may be
        improved to generate only a single query in a future release).
        """
        clone = self._clone()
        if defer:
            clone._iterable_class = DeferredSpecificIterable
        else:
            clone._iterable_class = SpecificIterable
        return clone

