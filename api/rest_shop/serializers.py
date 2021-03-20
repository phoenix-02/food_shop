from django.contrib.auth.models import User, Group
from rest_framework import serializers

from shop.models import Dish, Company, Cart, CartContent


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['url', 'id', 'title']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['url', 'id', 'title']


class DishSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    company = CompanySerializer()
    depth = 1

    class Meta:
        model = Dish
        fields = ['id', 'title', 'url', 'company', 'categories']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class CartContentSerializer(serializers.ModelSerializer):
    product = DishSerializer()

    class Meta:
        model = CartContent
        fields = '__all__'


class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer
    cart_content = CartContentSerializer(source='get_cart_content', many=True)
    depth = 1

    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_content')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
