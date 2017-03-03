from django.db import models

from .product_type_model import ProductTypeModel

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    product_type = models.ForeignKey(ProductTypeModel, on_delete=models.CASCADE,)