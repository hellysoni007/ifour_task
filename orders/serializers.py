from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from discounts.models import Discount

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    discounts = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all(), many=True)

    class Meta:
        model = Order
        fields = ['user', 'items', 'discounts', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        discounts_data = validated_data.pop('discounts')
        
        order = Order.objects.create(**validated_data)
        
        # Create OrderItems and add them to the order
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        
        # Add discounts to the order
        for discount in discounts_data:
            order.discounts.add(discount)

        return order
