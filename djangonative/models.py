from turtle import title
from django.db import models

# Create your models here.

class Note(models.Model):
    body=models.TextField(null=True,blank=True)
    update=models.DateTimeField(auto_now=True)
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.body[0:50]

class Test(models.Model):
    title=models.CharField(max_length=30)
    complete=models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self) :
        return self.title