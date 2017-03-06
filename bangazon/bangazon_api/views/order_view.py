from rest_framework import viewsets
from bangazon_api.models.order_model import OrderModel
from bangazon_api.serializers.order_serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):

    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
