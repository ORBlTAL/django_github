from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name= 'index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
]
