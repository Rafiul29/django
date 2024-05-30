from django.shortcuts import render
from .forms import MusicianForm
# Create your views here.

def add_musician(request):
  form=MusicianForm()
  return render(request,'add_musician.html',{'form':form})