from rest_framework import serializers
from .models import Cart, CartItem
from catalog.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=CartItem.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'product_id', 'quantity']
