from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)  
    vendor = models.CharField(max_length=255)  
    category = models.CharField(max_length=100)  
    image_srcs = models.JSONField(default=list)  
    sizes = models.JSONField(default=list)  

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    orderID = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.orderID} by {self.user.username}"
