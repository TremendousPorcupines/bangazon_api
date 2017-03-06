from rest_framework import viewsets
from models.order_model import OrderModel
from serializers.order_serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):

    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
