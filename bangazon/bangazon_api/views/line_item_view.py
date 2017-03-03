from rest_framework import viewsets
from models.line_item_model import LineItemModel

class LineItemModelViewSet(viewsets.ModelViewSet):
    queryset = LineItemModel.objects.all()
    serializer_class = LineItemModelSerializer