from rest_framework.pagination import PageNumberPagination


class WeekDayPagination(PageNumberPagination):
    page_size = 7
