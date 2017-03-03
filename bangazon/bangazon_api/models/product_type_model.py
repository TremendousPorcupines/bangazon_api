from django.db import models

class ProductTypeModel(models.Model):
    name = models.CharField(max_length=100)