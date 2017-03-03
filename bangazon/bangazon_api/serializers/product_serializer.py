from rest_framework import serializers
from .models.product_model import ProductModel

class ProductModelSerializer(serializers.Serializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'description', 'price', 'product_type')
