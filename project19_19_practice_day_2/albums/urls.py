from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_album/',views.AddAlbumCreateView.as_view(),name='add_album'),
    path('edit/<int:id>',views.EditAlbumView.as_view(),name='editalbum'),
    path('delete/<int:id>',views.DeleteAlbumView.as_view(),name='deletealbum')
]
