from distutils.command.upload import upload
from operator import mod
from sre_constants import CATEGORY
from turtle import title
from django.db import models

# Create your models here.

# class Note(models.Model):
#     body=models.TextField(null=True,blank=True)
#     update=models.DateTimeField(auto_now=True)
#     create=models.DateTimeField(auto_now_add=True)

#     def __str__(self) :
#         return self.body[0:50]

# class Test(models.Model):
#     title=models.CharField(max_length=30)
#     complete=models.BooleanField(default=False, blank=True, null=True)
#     upload = models.ImageField(upload_to ='uploads/')
    
#     def __str__(self) :
#         return self.title

class Person(models.Model):
    username = models.CharField(max_length=30)
    number = models.IntegerField()
    email = models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    longitude = models.FloatField( null=True)
    latitude = models.FloatField( null=True)
    dispatch_mode=models.BooleanField()




        


    

class Restaurant(models.Model):
   
    name=models.CharField(max_length=30)
    rating=models.CharField(max_length=30)
    image = models.ImageField(upload_to ='uploads/')
    location=models.CharField(max_length=30)
    
    def __str__(self) :
        return self.name 

    


class Dishes(models.Model):
    restaurantName=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self) :
        return self.name
        




    