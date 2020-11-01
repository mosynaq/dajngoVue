# import graphene
# from graphene_django import DjangoObjectType
# from app import models
#
#
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = models.Author
#         fields = ("id", "first_name", "last_name", "date_of_birth", "bio",)
#
#
# class WorkOfArtType(DjangoObjectType):
#     class Meta:
#         model = models.WorkOfArt
#         fields = ("id", "title", "type", "author", "description", "rating", "image", "price",)
#
#
# class Query(graphene.ObjectType):
#     all_works_of_art = graphene.List(WorkOfArtType)
#     author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
#     all_authors = graphene.List(AuthorType)
#
#     def resolve_all_works_of_art(root, info):
#         return models.WorkOfArt.objects.select_related("author").all()
#
#     def resolve_author_by_id(root, info, id):
#         try:
#             return models.Author.objects.get(id=id)
#         except models.Author.DoesNotExist:
#             return None
#
#     def resolve_all_authors(root,info):
#         return models.Author.objects.all()
#
#
# schema = graphene.Schema(query=Query)
#
#
#
#
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from app.models import Author, WorkOfArt


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ['first_name', 'last_name', 'last_name']
        interfaces = (relay.Node,)


class WorkOfArtNode(DjangoObjectType):
    class Meta:
        model = WorkOfArt
        # Allow for some more advanced filtering here
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
            'type': ['exact'],
            'author__first_name': ['exact'],
            'author__last_name': ['exact'],
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    author = relay.Node.Field(AuthorNode)
    all_authors = DjangoFilterConnectionField(AuthorNode)

    works_of_art = relay.Node.Field(WorkOfArtNode)
    all_works_of_art = DjangoFilterConnectionField(WorkOfArtNode)
