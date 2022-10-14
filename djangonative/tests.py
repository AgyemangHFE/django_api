from django.test import TestCase 
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .import views
from rest_framework.test import APITestCase
from rest_framework import status
from djangonative.urls import path

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_api_overview(self):
        
        url=reverse('api-overview')
        
        self.assertEquals(resolve(url).func,views.apiOverview)
    
    def test_api_task_list(self):
       
        url=reverse('task-list')
        
        self.assertEquals(resolve(url).func,views.tasklist)

    def test_api_order_list(self):
        
        url=reverse('order-list')
        
        self.assertEquals(resolve(url).func,views.orders)

       

    
    def test_api_restaurant_list(self):
        
        url=reverse('restaurant-list')
        
        self.assertEquals(resolve(url).func,views.restaurantlist)
    
    def test_api_register_person(self):
        
        url=reverse('register-person')
        
        self.assertEquals(resolve(url).func,views.registerperson)
    
    def test_api_create_task(self):
        
        url=reverse('task-create')
        
        self.assertEquals(resolve(url).func,views.taskCreate)

    def test_api_delete_task(self):
        
        url=reverse('person-list')
        
        self.assertEquals(resolve(url).func,views.personlist)