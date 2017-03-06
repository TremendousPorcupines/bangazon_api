from rest_framework import viewsets
from bangazon_api.serializers.product_serializer import ProductSerializer
from bangazon_api.models.product_model import ProductModel

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
