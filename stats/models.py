from django.core.validators import MinValueValidator
from django.db import models

from customers.models import Customer
from products.models import Product
from users.models import User


class Commerce(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(0)])
    total_price = models.FloatField(validators=[MinValueValidator(0)])
    paid_price = models.FloatField(validators=[MinValueValidator(0)], default=0)
    debt = models.FloatField(validators=[MinValueValidator(0)], default=0)
    description = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.store_name}: {self.product.name}[{self.amount}]"
