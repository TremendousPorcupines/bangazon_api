from django.db import models

class ProductType(models.Model):
    name = CharField(max_length=100)