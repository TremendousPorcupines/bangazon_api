from django.db import models

class LineItem(models.Model):
    order = ForeignKey(Order, on_delete=models.CASCADE,)
    product = ForeignKey(Product, on_delete=models.CASCADE,)