from django.contrib import admin 
from django.urls import path 
from .views import sayHello, index, bookingView, menuView
  
urlpatterns = [ 
    path('', index, name='index'),
    path('', sayHello, name='sayHello'), 
    path('menu/',menuView.as_view(), name='menu'),
    path('booking/', bookingView.as_view(), name='booking'),
]