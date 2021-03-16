import graphene
from api.graphql_shop.all_mutations.dish import CreateDish, UpdateDish
from api.graphql_shop.all_mutations.cart import CreateCart, UpdateCart


class Mutation(graphene.ObjectType):
    create_dish = CreateDish.Field()
    update_dish = UpdateDish.Field()
    create_cart = CreateCart.Field()
    update_cart = UpdateCart.Field()
