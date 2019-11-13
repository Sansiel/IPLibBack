from rest_framework.generics import ListCreateAPIView
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers
from django.contrib.auth.models import User
from .models import Book
from .book import BookRepository


class AuthorViewSet(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookViewSet(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        querystring = self.request.query_params.get('q')

        if querystring is not None:
            return BookRepository.search(querystring)

        return Book.objects.all()

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

class FileUploadView(APIView):
    permission_classes = [AllowAny]
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = serializers.FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)