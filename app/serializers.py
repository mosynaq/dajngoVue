from . import models
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("first_name", "last_name", "date_of_birth",)


class WorkOfArtSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = models.WorkOfArt
        fields = ("id", "title", "type", "author",)
