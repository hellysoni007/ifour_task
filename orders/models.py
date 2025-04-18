from django.db import models
from products.models import Product
from users.models import User
from discounts.models import Discount

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    discounts = models.ManyToManyField(Discount, blank=True)

    def calculate_total(self):
        """
        Calculate the total price of the order, applying discounts.
        """
        order_total = 0

        for item in self.items.all():
            order_total += item.product.get_price(item.quantity)

        # Apply each discount based on its priority
        sorted_discounts = self.discounts.all().order_by('priority')
        
        for discount in sorted_discounts:
            for item in self.items.all():
                order_total = discount.apply_discount(order_total, item.quantity)

        return order_total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
