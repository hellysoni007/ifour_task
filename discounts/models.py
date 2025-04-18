from django.db import models

class Discount(models.Model):
    TYPES = [('percentage', 'Percentage'), ('fixed', 'Fixed'), ('tiered', 'Tiered')]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPES)
    value = models.FloatField()  # For percentage or fixed discount value
    priority = models.IntegerField()

    def apply_discount(self, order_total, quantity=None):
        """
        Apply the discount based on its type.
        """
        if self.type == 'percentage':
            return order_total * (1 - self.value / 100)
        elif self.type == 'fixed':
            return order_total - self.value
        elif self.type == 'tiered':
            return self.apply_tiered_discount(order_total, quantity)
        return order_total
    
    def apply_tiered_discount(self, order_total, quantity):
        """
        Apply tiered discount based on the product quantity or order total.
        """
        if quantity is None:
            return order_total  # In case of a non-quantity-based tiered discount
        
        # Tiered discount based on quantity
        if quantity >= 51:
            return order_total * (1 - 0.15)  # 15% off for 51+ units
        elif quantity >= 21:
            return order_total * (1 - 0.10)  # 10% off for 21-50 units
        elif quantity >= 10:
            return order_total * (1 - 0.05)  # 5% off for 10-20 units
        
        return order_total
