import graphene
from api.graphql_shop.all_queries.dish import DishType
from api.graphql_shop.all_mutations.company import CompanyInput
from shop.models import Dish


class DishInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    company = graphene.List(CompanyInput)
    categories = graphene.List(graphene.ID)
    description = graphene.String()
    price = graphene.Int()


class CreateDish(graphene.Mutation):
    class Arguments:
        dish = DishInput(required=True)

    dish = graphene.Field(DishType)

    @staticmethod
    def mutate(self,info,dish=None):
        # m2m graphql requires
        categories = dish.pop("categories")
        dish_instance = Dish(**dish)
        dish_instance.save()
        dish_instance.categories.set(categories)
        return CreateDish(dish=dish_instance)


class UpdateDish(graphene.Mutation):
    class Arguments:
        dish = DishInput(required=True)

    dish = graphene.Field(DishType)

    @staticmethod
    def mutate(self,info,dish=None):
        dish_instance = Dish.objects.get(pk=dish.id)
        if dish_instance:
            categories = dish.pop("categories")
            dish_instance = Dish(**dish)
            dish_instance.save()
            dish_instance.categories.set(categories)
            return UpdateDish(dish=dish_instance)
        return UpdateDish(dish=None)
