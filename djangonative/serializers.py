from rest_framework import serializers
from .models import Dishes, Person, Restaurant, Test

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields ='__all__'

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields ='__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields ='__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields ='__all__'