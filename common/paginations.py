# coding:utf-8
__author__ = 'Luo'

from rest_framework.pagination import PageNumberPagination


class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 40