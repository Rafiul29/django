from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('register/',views.UserCreateView.as_view(),name='register'),
  path('login/',views.UserLoginView.as_view(),name='login'),
  path('profile/',views.Profile.as_view(),name='profile'),
  path('logout/',views.UserLogoutView.as_view(),name='logout'),
]


