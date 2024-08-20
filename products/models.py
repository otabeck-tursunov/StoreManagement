from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True, null=True)
    import_price = models.FloatField(validators=[MinValueValidator(0), ])
    export_price = models.FloatField(validators=[MinValueValidator(0), ])
    amount = models.FloatField(validators=[MinValueValidator(0), ])
    unit = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ImportProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    import_price = models.FloatField(validators=[MinValueValidator(0), ])
    amount = models.FloatField(validators=[MinValueValidator(0), ])
    total_price = models.FloatField(validators=[MinValueValidator(0), ])
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name) + str(self.amount)


