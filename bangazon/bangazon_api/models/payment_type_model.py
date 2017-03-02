from django.db import models
from django.contrib.auth.models import User


class PaymentType(models.Model):
    name = models.CharField()
    number = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
