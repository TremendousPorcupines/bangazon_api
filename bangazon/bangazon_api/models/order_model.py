from django.db import models
from django.contrib.auth.models import User
from .payment_type_model import PaymentTypeModel

class OrderModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(
        PaymentTypeModel,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    completed = models.BooleanField(default = False)
