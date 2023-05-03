from rest_framework.pagination import PageNumberPagination


class JewelryPaginator(PageNumberPagination):
    page_size = 20
