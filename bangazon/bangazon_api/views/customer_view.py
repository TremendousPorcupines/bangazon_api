from rest_framework import viewsets
from bangazon_api.serializers.customer_serializer import CustomerSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
import json
from django.http import HttpResponse


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = CustomerSerializer


class IsAuth(GenericAPIView):

    def get(self, request, **kwargs):
        if self.request.user.is_anonymous:
            response = json.dumps({"user": False})
        else:
            response = json.dumps({
                "user": True,
                "user_id": self.request.user.pk,
                "username": self.request.user.username,
            })
        return HttpResponse(response, content_type='application/json')
