from rest_framework import serializers
from models.order_model import OrderModel
from models.payment_type_model import PaymentTypeModel

class LineItemSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = LineItemModel
        fields = ('id', 'order', 'product')