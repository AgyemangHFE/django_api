from django.test import TestCase 
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .import views
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class APITesting(APITestCase):
    def test_api_list(self):
        response=self.client.get(reverse('api-overview'))
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class APITesting(APITestCase):
    def test_api_list(self):
        response=self.client.get(reverse('task-list'))
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
 
class APITesting(APITestCase):
    def test_api_list(self):
        response=self.client.get(reverse('dispatch-list'))
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class APITesting(APITestCase):
    def test_api_list(self):
        response=self.client.get(reverse('person-list'))
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)

