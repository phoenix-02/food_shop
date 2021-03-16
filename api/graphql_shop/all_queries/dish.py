import graphene
from django.contrib.postgres.search import SearchVector
from graphene_django.types import DjangoObjectType, ObjectType
from shop.models import Dish


class DishType(DjangoObjectType):
    class Meta:
        model = Dish


class Query(ObjectType):
    dish = graphene.Field(DishType, id=graphene.Int())
    dishes = graphene.List(DishType)

    @staticmethod
    def resolve_dish(self, info, **kwargs):
        dish_id = kwargs.get('dish_id')
        if dish_id is not None:
            return Dish.objects.get(pk=dish_id)
        return None

    @staticmethod
    def resolve_dishes(self, info, **kwargs):
        return Dish.objects.all()

    @staticmethod
    def resolve_dish_search(self, info, **kwargs):
        string = kwargs.get("string", "")
        search_vector = SearchVector('title',
                                     'description',
                                     'categories__title',
                                     'company__title', )
        return Dish.objects.annotate(search=search_vector).filter(search=string)
