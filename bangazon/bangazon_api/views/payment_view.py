from rest_framework import viewsets
from serializers.payment_type_serializer import PaymentTypeSerializer
from models.payment_type_model import PaymentTypeModel

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = PaymentTypeModel.objects.all()
    serializer_class = PaymentTypeSerializer
