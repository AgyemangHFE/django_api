import imp
import re
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dishes, Restaurant, Test

from djangonative.models import Test
from .serializers import RestaurantSerializer, TaskSerializer,DishSerializer

@api_view(['GET'])
def tasklist(request):
    task=Test.objects.all()
    serializer=TaskSerializer(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task=Test.objects.get(id=pk)
    serializer=TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task=Test.objects.get(id=pk)
    
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task=Test.objects.get(id=pk)
    
    task.delete()

    return Response('Deleted')

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'list':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk/>'

    }
    return Response(api_urls)


@api_view(['GET'])
def dishlist(request):
    dish=Dishes.objects.all()
    serializer=DishSerializer(dish,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dishDetail(request,pk):
    dish=Dishes.objects.filter(restaurantName=pk)
    serializer=DishSerializer(dish,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def restaurantlist(request):
    res=Restaurant.objects.all()
    serializer=RestaurantSerializer(res,many=True)
    return Response(serializer.data)




# Create your views here.
