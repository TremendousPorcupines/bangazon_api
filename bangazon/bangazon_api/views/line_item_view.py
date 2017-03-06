from rest_framework import viewsets
from bangazon_api.serializers.line_item_serializer import LineItemSerializer
from bangazon_api.models.line_item_model import LineItemModel

class LineItemViewSet(viewsets.ModelViewSet):
    queryset = LineItemModel.objects.all()
    serializer_class = LineItemSerializer
