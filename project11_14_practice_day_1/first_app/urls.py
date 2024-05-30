from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('forms_api/',views.forms_api,name='forms_api'),
    path('model_froms/',views.model_froms,name='model_froms')
]
