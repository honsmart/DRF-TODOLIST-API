from rest_framework import pagination


class CustomPageNumberPagination(pagination.PageNumberPagination):
      page_size=15
      page_query_description='count'
      max_page_size=15
      page_query_param = 'p'
