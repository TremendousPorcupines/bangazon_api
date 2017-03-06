from rest_framework import viewsets
from bangazon_api.serializers.product_type_serializer import ProductTypeSerializer
from bangazon_api.models.product_type_model import ProductTypeModel

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductTypeModel.objects.all()
    serializer_class = ProductTypeSerializer
