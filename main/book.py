from django.contrib.postgres.search import SearchVector
from django.db.models import QuerySet

from .models import Book


class BookRepository:
    @classmethod
    def search(cls, querystring: str) -> QuerySet:
        qs = Book.objects \
            .select_related('author') \
            .annotate(search=SearchVector('title', 'author__first_name', 'author__last_name')) \
            .filter(search=querystring)
        return qs