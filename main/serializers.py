from rest_framework import serializers

from . import models

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = models.Book
        fields = (
            'id',
            'author',
            'title',
        )