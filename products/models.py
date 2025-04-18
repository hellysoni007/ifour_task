from django.db import models
import datetime

class Product(models.Model):
    TYPES = [
        ('base', 'Base'),
        ('seasonal', 'Seasonal'),
        ('bulk', 'Bulk'),
        ('premium', 'Premium'),
    ]
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=TYPES, default='base')

    def get_price(self, quantity=None):
        """
        Return the base price for a product or adjusted price based on type.
        """
        if self.type == 'seasonal':
            return self.get_seasonal_price()
        elif self.type == 'bulk' and quantity:
            return self.get_bulk_price(quantity)
        elif self.type == 'premium':
            return self.get_premium_price()
        return self.base_price

    def get_seasonal_price(self):
        # Get the current month
        current_month = datetime.datetime.now().month
        
        # Winter discount (Dec, Jan, Feb)
        if 12 <= current_month <= 2:
            return self.base_price * 0.8  # 20% off during winter
        return self.base_price
    
    def get_bulk_price(self, quantity):
        """
        Returns price based on the quantity purchased for bulk products.
        """
        price = self.base_price * quantity
        
        # Apply tiered discount
        if quantity >= 51:
            return price * 0.85  # 15% off for 51+ units
        elif quantity >= 21:
            return price * 0.9  # 10% off for 21-50 units
        elif quantity >= 10:
            return price * 0.95  # 5% off for 10-20 units
        
        return price
    
    def get_premium_price(self):
        premium_markup = 0.15  # 15% markup for premium features
        return self.base_price * (1 + premium_markup)  # Apply markup