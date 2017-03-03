from django.db import models

from .product_model import Product
from .order_model import Order

class LineItem(models.Model):
    order = ForeignKey(Order, on_delete=models.CASCADE,)
    product = ForeignKey(Product, on_delete=models.CASCADE,)