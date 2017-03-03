from rest_framework import serializers
from .models.product_type_model import ProductTypeModel

class ProductTypeSerializer(serializers.Serializer):
    class Meta:
        model = ProductModelType
        fields = ('id', 'name')
