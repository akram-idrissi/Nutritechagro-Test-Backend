from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)  
    vendor = models.CharField(max_length=255)  
    category = models.CharField(max_length=100)  
    image_srcs = models.JSONField(default=list)  
    sizes = models.JSONField(default=list)  

    def __str__(self):
        return self.name
