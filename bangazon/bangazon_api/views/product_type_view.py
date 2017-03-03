from rest_framework import viewsets
from models.product_type_model import ProductTypeModel

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductTypeModel.objects.all()
    serializer_class = ProductTypeModelSerializer