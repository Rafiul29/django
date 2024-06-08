from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_musician/',views.AddMusicianCreateView.as_view(),name='add_musician'),
    path('edit/<int:id>',views.EditMusicianView.as_view(),name='editmusician'),
]
