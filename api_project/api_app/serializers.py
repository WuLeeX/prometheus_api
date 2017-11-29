from rest_framework import serializers
from .models import Host

# Using ModelSerializer to keep our code a bit more concise
class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

