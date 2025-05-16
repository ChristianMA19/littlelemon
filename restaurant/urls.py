from django.contrib import admin 
from django.urls import path 
from .views import sayHello, index 
  
urlpatterns = [ 
    path('', index, name='index'),
    path('', sayHello, name='sayHello'), 
]