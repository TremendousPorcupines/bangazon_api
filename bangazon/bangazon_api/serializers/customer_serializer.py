from rest_framework import serializers
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name',
            'password', 'email', 'username',
        )
