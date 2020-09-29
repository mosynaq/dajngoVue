from rest_framework.pagination import PageNumberPagination, CursorPagination as DRFCursorPagination


class CursorPagination(DRFCursorPagination):
    ordering = "id"
