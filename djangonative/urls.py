from django.urls import path
from .import views

urlpatterns =[
    path('',views.apiOverview,name='api-overview'),
    path('task-list/',views.tasklist,name='task-list'),
    path('task-detail/<str:pk>/',views.taskDetail,name='task-detail'),
    path('task-create/',views.taskCreate,name='task-create'),
    path('task-update/<str:pk>/',views. taskUpdate,name='task-update'),
    path('task-delete/<str:pk>/',views. taskDelete,name='task-Delete'),
    path('dish-list/',views.dishlist,name='dish-list'),
    path('dish-detail/<str:pk>/',views.dishDetail,name='dish-detail'),
    path('restaurant-list/',views.restaurantlist,name='restaurant-list'),
    
]