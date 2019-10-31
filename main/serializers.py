from rest_framework import serializers

from . import models
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'is_staff': UserSerializer(user, context={'request': request}).data['is_staff']
    } 