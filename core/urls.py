from django.urls import path 
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('sortear/', views.sortear, name='sortear'),
    path('cartelas/', views.cartelas, name='cartelas'), 
]