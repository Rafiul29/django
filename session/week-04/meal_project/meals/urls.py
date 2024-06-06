from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_meals,name='home'),
    path('add_meal/',views.add_meals,name='add_meal'),
]
