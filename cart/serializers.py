from rest_framework import serializers

from base.serializers.base_serializers import ModelSerializer
from products.serializers import ProductQuantitiesSerializer

from .models import *


class CartItemGetSerializer(ModelSerializer):
    product_quantity = ProductQuantitiesSerializer()

    class Meta:
        model = CartItem
        exclude = ('cart',)


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        exclude = ('cart',)

    def create(self, validated_data):
        user = self.context['user']
        cart_obj = Cart.objects.get_or_create(user=user)
        item = CartItem.objects.filter(
            cart=cart_obj, product_quantity=validated_data['product_quantity'])
        if item.exists():
            item = item.first()
            item.quantity += validated_data['quantity']
            item.save()
            return item

        validated_data['cart'] = cart_obj
        return CartItem.objects.create(**validated_data)


class CartSerializer(ModelSerializer):
    items = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        exclude = ('user',)

    def get_items(self, obj):
        return CartItemSerializer(obj.productscartitem_set.all(), many=True).data

    def get_price(self, obj):
        return obj.get_cart_price()
