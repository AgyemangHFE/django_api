import imp
import re
from trace import Trace
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dishes, Person, Restaurant, Test

from djangonative.models import Test
from .serializers import RestaurantSerializer, TaskSerializer,DishSerializer,PersonSerializer

@api_view(['GET'])
def personlist(request):
    task=Person.objects.all()
    serializer=PersonSerializer(task,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerperson(request):
    
    serializer=PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def dispatchlist(request):
    task=Person.objects.filter(dispatch_mode=True)
    serializer=PersonSerializer(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dispatchOn(request,pk):
    task=Person.objects.filter(id=pk).update(dispatch_mode=True)
    return Response("Dispatch Mode On") 
@api_view(['GET'])
def dispatchOff(request,pk):
    task=Person.objects.filter(id=pk).update(dispatch_mode=False)
    return Response("Dispatch Mode Off") 




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
        'Delete':'/task-delete/<str:pk/>',

        'Dishes':'dish-detail/<str:pk>/',
        'DispatchList':'dispatch-list/',
        'DispatchOn':'dispatch-on<str:pk>/',
        'DispatchOff':'dispatch-off<str:pk>/',
        'RestaurantList':'restaurant-list/',
        'Register':'register-person/',
        'PersonList':'person-list/',

    }
    return Response(api_urls)


@api_view(['GET'])
def dishlist(request):
    dish=Person.objects.all()
    serializer=PersonSerializer(dish,many=True)
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
