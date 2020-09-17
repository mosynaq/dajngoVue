from rest_framework import viewsets
from .models import Author, WorkOfArt
from . import serializers


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class WorkOfArtViewSet(viewsets.ModelViewSet):
    queryset = WorkOfArt.objects.all()
    serializer_class = serializers.WorkOfArtSerializer
