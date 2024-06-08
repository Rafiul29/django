from django.shortcuts import render
from musicians.models import Musician
from albums.models import Album

def home(request):
  data=Album.objects.all()
  return render(request,'home.html',{'data':data})