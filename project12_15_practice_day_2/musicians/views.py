from django.shortcuts import render
from .forms import MusicianForm
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
 