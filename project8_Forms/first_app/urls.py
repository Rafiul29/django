from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="homepage"),
    path("about/", views.about,name="aboutpage"),
    path("singup/", views.signup,name="singuppage"),
    path("django_form/",views.djangoForm,name="djangoForm"),
    path("student_form/",views.StudentForm,name="StudentForm"),
]
