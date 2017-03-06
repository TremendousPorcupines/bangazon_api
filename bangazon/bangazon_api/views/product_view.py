from rest_framework import viewsets
from serializers.product_serializer import ProductSerializer
from models.product_model import ProductModel

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer