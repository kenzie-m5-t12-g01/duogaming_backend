from rest_framework.pagination import PageNumberPagination


class GamesPagination(PageNumberPagination):
    page_size = 6
