from rest_framework import viewsets
from serializers.customer_serializer import CustomerSerializer
from django.contrib.auth.models import User


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = CustomerSerializer
