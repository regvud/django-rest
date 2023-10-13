import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_query_param = 'page'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = math.ceil(count / self.page_size)

        resp = {
            'total_items': count,
            'total_pages': total_pages,
            'prev': self.get_previous_link(),
            'next': self.get_next_link(),
            'data': data

        }

        return Response(resp, status=200)
