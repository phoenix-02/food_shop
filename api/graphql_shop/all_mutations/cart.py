import graphene

from api.graphql_shop.all_queries.cart import CartType
from shop.models import Cart


class CartInput(graphene.InputObjectType):
    id = graphene.ID()
    session_key = graphene.String()
    total_cost = graphene.Int()


class CreateCart(graphene.Mutation):
    class Arguments:
        cart = CartInput(required=True)

    cart = graphene.Field(CartType)

    @staticmethod
    def mutate(self,info,cart=None):
        cart_instance = Cart(**cart)
        cart_instance.save()
        return CreateCart(dish=cart_instance)


class UpdateCart(graphene.Mutation):
    class Arguments:
        cart = CartInput(required=True)

    cart = graphene.Field(CartType)

    @staticmethod
    def mutate(self,info,cart=None):
        cart_instance = Cart(**cart)
        cart_instance.save()
        return UpdateCart(dish=cart_instance)
