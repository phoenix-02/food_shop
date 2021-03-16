import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from shop.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(ObjectType):
    category = graphene.Field(CategoryType, id=graphene.Int())
    categories = graphene.List(CategoryType)

    @staticmethod
    def resolve_category(self, info, **kwargs):
        category_id = kwargs.get('dish_id')
        if category_id is not None:
            return Category.objects.get(pk=category_id)
        return None

    @staticmethod
    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()
