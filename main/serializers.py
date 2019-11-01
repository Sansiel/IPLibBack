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
    
    def create(self, validated_data):
        return models.Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)


        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = models.Book
        fields = (
            'id',
            'author',
            'title',
        )

    def create(self, validated_data):
        authors_data = validated_data.pop('author')
        order = models.Book.objects.create(**validated_data)
        for author_data in authors_data:
            models.Author.objects.create(order=order, **author_data)
        return order        

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

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = "__all__"