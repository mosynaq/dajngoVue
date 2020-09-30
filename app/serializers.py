from . import models
from rest_framework import serializers
from rest_framework.fields import DateField


class AuthorSerializer(serializers.ModelSerializer):
    # '2013-01-29T12:34:56.000000Z
    # date_of_birth = DateField(format="%Y-%m-%dT00:00:00.000000Z")

    class Meta:
        model = models.Author
        fields = ("id", "first_name", "last_name", "date_of_birth", "bio",)


class WorkOfArtSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = models.WorkOfArt
        fields = ("id", "title", "type", "author", "description", "rating", "image", "price",)
