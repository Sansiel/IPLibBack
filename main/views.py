from rest_framework.generics import ListCreateAPIView

from . import models
from . import serializers


class AuthorViewSet(ListCreateAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookViewSet(ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(author_id=self.request.data['author_id'])

    def perform_update(self, serializer):
        serializer.save(author_id=self.request.data['author_id'])