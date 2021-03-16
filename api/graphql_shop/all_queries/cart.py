import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from shop.models import Cart


class CartType(DjangoObjectType):
    class Meta:
        model = Cart


class Query(ObjectType):
    cart = graphene.Field(CartType, id=graphene.Int())
    carts = graphene.List(CartType)

    @staticmethod
    def resolve_cart(self, info, **kwargs):
        cart_id = kwargs.get('dish_id')
        if cart_id is not None:
            return Cart.objects.get(pk=cart_id)
        return None

    @staticmethod
    def resolve_carts(self, info, **kwargs):
        return Cart.objects.all()
