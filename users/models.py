from django.db import models
from django.contrib.auth.models import AbstractUser


class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    branch_name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
    image_path = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.username
