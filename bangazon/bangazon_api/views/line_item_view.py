from rest_framework import viewsets
from bangazon_api.serializers.line_item_serializer import LineItemSerializer
from bangazon_api.models.line_item_model import LineItemModel

class LineItemViewSet(viewsets.ModelViewSet):
    serializer_class = LineItemSerializer

    def get_queryset(self, **kwargs):
        if self.request.user.is_staff:
            return LineItemModel.objects.all()
        else:
            products = LineItemModel.objects.filter(
                order__customer=self.request.user
            )
            return products
