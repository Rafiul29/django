from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_album/',views.AddAlbumCreateView.as_view(),name='add_album'),
    path('edit/<int:id>',views.edit_album,name='editalbum'),
    path('delete/<int:id>',views.delete_album,name='deletealbum')
]
