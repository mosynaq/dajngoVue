import graphene
from graphene_django import DjangoObjectType
from app import models


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Author
        fields = ("id", "first_name", "last_name", "date_of_birth", "bio",)


class WorkOfArtType(DjangoObjectType):
    class Meta:
        model = models.WorkOfArt
        fields = ("id", "title", "type", "author", "description", "rating", "image", "price",)


class Query(graphene.ObjectType):
    all_works_of_art = graphene.List(WorkOfArtType)
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
    all_authors = graphene.List(AuthorType)

    def resolve_all_works_of_art(self, root):
        return models.WorkOfArt.objects.select_related("author").all()

    def resolve_author_by_id(self, root, id):
        try:
            return models.Author.objects.get(id=id)
        except models.Author.DoesNotExist:
            return None

    def resolve_all_authors(self, root):
        return models.Author.objects.all()


schema = graphene.Schema(query=Query)
