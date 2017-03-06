from rest_framework import serializers
from bangazon_api.models.product_model import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = ProductModel
        fields = ('id', 'url', 'name', 'description', 'price', 'product_type')
