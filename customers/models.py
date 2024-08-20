from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    store_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    debt = models.FloatField(validators=[MinValueValidator(0)], default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.store_name}'
