"""
Custom Pagination for Django REST Framework

This module provides a custom pagination class for Django REST Framework.
It allows for customization of the number of objects returned per page
and supports a query parameter to specify the page size.

Classes:
    CustomPagination:
        A custom pagination class that extends DRF's PageNumberPagination.
"""

from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    """
    This class customizes the pagination behavior by allowing clients to
    specify the number of objects returned per page using a query parameter.

    Attributes:
        page_size (int): The default number of objects to return per page.
        page_size_query_param (str): The query parameter used by clients to
            specify the page size.
        max_page_size (int): The maximum number of objects that can be returned
            per page.
    """

    page_size = 10  # Number of objects to return per page
    # Custom query parameter to specify page size
    page_size_query_param = "page_size"
    max_page_size = 100
