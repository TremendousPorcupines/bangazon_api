from rest_framework import serializers
from models.order_model import OrderModel

class OrderSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = OrderModel
        fields = ('id', 'url', 'customer', 'payment_type', 'completed')
