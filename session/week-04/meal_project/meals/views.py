from django.shortcuts import render,redirect
from .forms import FoodForm
from . import models


# Create your views here.
def show_meals(request):
  foods=models.Food.objects.all()
  return render(request,'meals/index.html',{'data':foods})


def add_meals(request):
  print(request)
  if request.method=="POST":
    food_form=FoodForm(request.POST,request.FILES)
    if food_form.is_valid():
      print(food_form.cleaned_data)
      food_form.save()
      return redirect('home')
  else:
    food_form=FoodForm()
  return render(request,'meals/meals_add.html',{'form':food_form})
