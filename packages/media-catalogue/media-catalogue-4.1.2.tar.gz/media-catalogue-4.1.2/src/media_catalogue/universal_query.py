# -*- coding: utf-8 -*-

import warnings

from collections import defaultdict
from types import SimpleNamespace

from django.apps import apps
from django.db.models import Q, QuerySet
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import BaseIterable

from wagtail.search.backends import get_search_backend

from wagtail.search.queryset import SearchableQuerySetMixin

__all__ = ['UniversalMediaItemQuerySet']

"""
class ContentItemIterable(BaseIterable):
    def __iter__(self):
        return content_item_iterator(self.queryset, include_universal_pk=False)


class ContentItemWithUniversalPKIterable(BaseIterable):
    def __iter__(self):
        return content_item_iterator(self.queryset, include_universal_pk=True)
"""


def content_items_by_content_type_adapter(qs):

    values = qs.values('pk', 'content_type', 'content_id')

    entries_by_type = defaultdict(SimpleNamespace)

    for v in values:
        content_type = v['content_type']

        entry = entries_by_type[content_type]

        if not hasattr(entry, 'map_to_universal_pk'):
            entry.map_to_universal_pk = dict()

        entry.map_to_universal_pk[v['content_id']] = v['pk']

    for content_type, entry in entries_by_type.items():

        content_type = ContentType.objects.get_for_id(content_type)

        if not content_type:
            continue

        entry.model = content_type.model_class()
        # entry.query_set = entry.model.objects.in_bulk(id_list=entry.map_to_universal_pk.keys())  # model.objects.filter(pk__in=entry.map_to_universal_pk)

    return entries_by_type


def search_iterator(query_set, query, fields=None, operator=None, order_by_relevance=True, partial_match=True, backend='default'):

        from .models.universal_media_items import UniversalMediaItem

        search_backend = get_search_backend(backend)

        for content_type, entry in content_items_by_content_type_adapter(query_set).items():
            entry.query_set = search_backend.search(query, entry.model.objects.all(), fields=fields, operator=operator,
                                                    order_by_relevance=order_by_relevance, partial_match=partial_match)

            for result in entry.query_set:  # .in_bulk(id_list=entry.map_to_universal_pk.keys()).values():
                universal_pk = entry.map_to_universal_pk[result.pk]
                universal_item = UniversalMediaItem.objects.get(pk=universal_pk)
                yield universal_item

            # result_pks = [entry.map_to_universal_pk[result.pk] for result in entry.query_set]

            # for item in UniversalMediaItem.objects.filter(pk__in=result_pks):
            #    yield item


class SearchIterable(BaseIterable):

    def __init__(self, queryset, query, fields=None, operator=None, order_by_relevance=True, partial_match=True, backend='default', **kwargs):

        super(SearchIterable, self).__init__(queryset, **kwargs)

        self.query = query
        self.fields = fields
        self.operator = operator
        self.order_by_relevance = order_by_relevance
        self.partial_match = partial_match
        self.backend = backend

    def __iter__(self):
        return search_iterator(self.queryset, self.query, self.fields, self.operator, self.order_by_relevance, self.partial_match, self.backend)


def create_search_iterable(queryset, query=None, fields=None, operator=None, order_by_relevance=True, partial_match=True, backend='default', **kwargs):
    return SearchIterable(queryset, query, fields, operator, order_by_relevance, partial_match, backend, **kwargs)


def autocomplete_iterator(query_set, query, fields=None, operator=None, order_by_relevance=True, backend='default'):

        from .models.universal_media_items import UniversalMediaItem

        search_backend = get_search_backend(backend)

        for content_type, entry in content_items_by_content_type_adapter(query_set).items():
            entry.query_set = search_backend.autocomplete(query, entry.query_set, fields=fields, operator=operator,
                                                          order_by_relevance=order_by_relevance)

            for result in entry.query_set:
                universal_pk = entry.map_to_universal_pk[result.pk]
                universal_item = UniversalMediaItem.objects.get(pk=universal_pk)
                yield universal_item

            # result_pks = [entry.map_to_universal_pk[result.pk] for result in entry.query_set]

            # for item in UniversalMediaItem.objects.filter(pk__in=result_pks):
            #    yield item


class AutocompleteIterable(BaseIterable):

    def __init__(self, queryset, query, fields=None, operator=None, order_by_relevance=True, backend='default', **kwargs):

        super(AutocompleteIterable, self).__init__(queryset, **kwargs)

        self.query = query
        self.fields = fields
        self.operator = operator
        self.order_by_relevance = order_by_relevance
        self.backend = backend

    def __iter__(self):
        return autocomplete_iterator(self.queryset, self.query, self.fields, self.operator, self.order_by_relevance, self.backend)


def create_autocomplete_iterable(queryset, query=None, fields=None, operator=None, order_by_relevance=True, backend='default', **kwargs):
    return AutocompleteIterable(queryset, query, fields, operator, order_by_relevance, backend, **kwargs)


class UniversalMediaItemQuerySet(QuerySet):

    # noinspection PyMethodMayBeStatic
    def universal_media_item_q(self, other):
        return Q(id=other.id)

    def universal_media_item(self, other):
        """
        This filters the QuerySet so it only contains the specified media item.
        """
        return self.filter(self.universal_media_item_q(other))

    def not_universal_media_item(self, other):
        """
        This filters the QuerySet so it doesn't contain the specified media_item.
        """
        return self.exclude(self.universal_media_item_q(other))

    # noinspection PyMethodMayBeStatic
    def type_q(self, klass):
        content_types = ContentType.objects.get_for_models(*[
            model for model in apps.get_models()
            if issubclass(model, klass)
        ]).values()

        return Q(content_type__in=list(content_types))

    def type(self, model):
        """
        This filters the QuerySet to only contain media items that are an instance
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

    def search(self, query, fields=None,
               operator=None, order_by_relevance=True, partial_match=True, backend='default'):

        clone = self._clone()
        clone._iterable_class = lambda queryset, **kwargs: create_search_iterable(
            queryset, query=query, fields=fields, operator=operator, order_by_relevance=order_by_relevance,
            partial_match=partial_match, backend=backend, **kwargs)

        return clone

    def autocomplete(self, query, fields=None,
                     operator=None, order_by_relevance=True, backend='default'):

        clone = self._clone()
        clone._iterable_class = lambda queryset, **kwargs: create_autocomplete_iterable(
            queryset, query=query, fields=fields, operator=operator, order_by_relevance=order_by_relevance,
            backend=backend, **kwargs)

        return clone

    """
    def filter(self, *args, **kwargs):

        for keyword in kwargs.keys():
            if keyword != 'tags' and not keyword.startswith('tags__'):
                continue

            

        return super(UniversalMediaItemQuerySet, self).filter(*args, **kwargs)
    """

"""
def content_items(self, include_universal_pks=False):

    clone = self._clone()
    clone._iterable_class = ContentItemWithUniversalPKIterable if include_universal_pks else ContentItemIterable
    return clone
"""
