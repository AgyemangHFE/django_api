from rest_framework import serializers
from .models import Test

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields ='__all__'