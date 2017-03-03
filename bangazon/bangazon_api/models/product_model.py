from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE,)