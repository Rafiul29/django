from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="homepage"),
    path("delete/<int:roll>",views.delete_student,name="delete_student"),
    path("create/",views.create,name="create_student"),
]