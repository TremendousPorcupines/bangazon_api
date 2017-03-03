from django.db import models

from .product_model import ProductModel
from .order_model import OrderModel

class LineItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE,)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,)