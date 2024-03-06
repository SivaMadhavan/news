from rest_framework.pagination import PageNumberPagination
from django.utils.functional import cached_property
from django.core.paginator import Paginator
from django.db.models.query import QuerySet


class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        if isinstance(self.object_list, QuerySet):
            return self.object_list.values("pk").count()
        else:
            return len(self.object_list)


class ListPagination(PageNumberPagination):
    """
    Pagination List pagination
    """

    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10
    default_page_size = 2
    django_paginator_class = FasterDjangoPaginator
