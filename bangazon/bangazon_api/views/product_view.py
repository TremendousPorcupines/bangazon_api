from rest_framework import viewsets
from models.product_model import ProductModel

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer