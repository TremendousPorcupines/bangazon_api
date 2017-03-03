from rest_framework import serializers
from models.product_type_model import ProductTypeModel

class ProductTypeSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = ProductModelType
        fields = ('id', 'name')
