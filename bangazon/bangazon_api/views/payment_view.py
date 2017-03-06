from rest_framework import viewsets
from bangazon_api.serializers.payment_type_serializer import PaymentTypeSerializer
from bangazon_api.models.payment_type_model import PaymentTypeModel

class PaymentTypeViewSet(viewsets.ModelViewSet):

    queryset = PaymentTypeModel.objects.all()
    serializer_class = PaymentTypeSerializer
