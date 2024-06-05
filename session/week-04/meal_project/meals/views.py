from django.shortcuts import render
from .forms import FoodForm
from . import models


# Create your views here.
def show_meals(request):
  foods=models.Food.objects.all()
  return render(request,'meals/index.html',{'data':foods})