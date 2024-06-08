from django.shortcuts import render,redirect
from .forms import MusicianForm
from . import models
# Create your views here.

def add_musician(request):
  if request.method=='POST':
    musician_form =MusicianForm(request.POST)
    if musician_form.is_valid():
      # print(musician_form.cleaned_data)
      musician_form.save()
  else:
    musician_form =MusicianForm()
  return render(request,'add_musician.html',{'form':musician_form})
 

def edit_musician(request,id):
  musician=models.Musician.objects.get(pk=id)
  print(musician.email)
  musician_form =MusicianForm(instance=musician)
  if request.method=='POST':
    musician_form =MusicianForm(request.POST,instance=musician)
    if musician_form.is_valid():
      # print(musician_form.cleaned_data)
      musician_form.save()
      return redirect('homepage')
  return render(request,'add_musician.html',{'form':musician_form})