from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'base_price', 'type']

class ProductPriceSerializer(serializers.ModelSerializer):
    calculated_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'base_price', 'type', 'calculated_price']

    def get_calculated_price(self, obj):
        quantity = self.context.get('quantity', 1)  # Default quantity to 1 if not provided
        return obj.get_price(quantity)