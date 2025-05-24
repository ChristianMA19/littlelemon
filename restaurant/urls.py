from django.contrib import admin 
from django.urls import path 
from .views import sayHello, index, bookingView, menuView
from rest_framework.authtoken import obtain_auth_token

from restaurant import views

  
urlpatterns = [ 
    path('', index, name='index'),
    path('', sayHello, name='sayHello'), 
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('menu/',menuView.as_view(), name='menu'),
    path('booking/', bookingView.as_view(), name='booking'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]