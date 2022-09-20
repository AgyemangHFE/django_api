from ast import Store
from this import d
from django.contrib import admin
from .models import Note,Test,Restaurant,Dishes,Person

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Dishes)
admin.site.register(Person)