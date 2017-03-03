from rest_framework import serializers
from models.product_model import ProductModel

class ProductModelSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'description', 'price', 'product_type')
