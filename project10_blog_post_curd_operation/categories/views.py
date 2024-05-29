from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_categories(request):
  if request.method=='POST':
    category_form=forms.CategoryForm(request.POST)
    if category_form.is_valid():
      # print(category_form.cleaned_data)
      category_form.save()
      return redirect("add_categories")
  else:
    category_form=forms.CategoryForm()
  return render(request,'add_category.html',{'form':category_form})