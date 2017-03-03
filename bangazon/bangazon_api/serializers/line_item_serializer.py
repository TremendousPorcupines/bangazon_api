from rest_framework import serializers
from models.line_item_model import LineItem

class LineItemSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = LineItemModel
        fields = ('id', 'url', 'order', 'product')