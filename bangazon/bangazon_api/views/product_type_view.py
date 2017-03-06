from rest_framework import viewsets
from serializers.product_type_serializer import ProductTypeSerializer
from models.product_type_model import ProductTypeModel

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductTypeModel.objects.all()
    serializer_class = ProductTypeSerializer