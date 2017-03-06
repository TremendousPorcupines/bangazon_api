from rest_framework import serializers
from bangazon_api.models.payment_type_model import PaymentTypeModel

class PaymentTypeSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = PaymentTypeModel
        fields = ('id', 'url', 'name', 'number', 'customer')
