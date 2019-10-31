from rest_framework.generics import ListCreateAPIView
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from . import models
from . import serializers
from django.contrib.auth.models import User


class AuthorViewSet(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookViewSet(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(author_id=self.request.data['author_id'])

    def perform_update(self, serializer):
        serializer.save(author_id=self.request.data['author_id'])

class UserList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer 