from django.shortcuts import render

# Create your views here.
def add_album(request):
  return render(request,'add_album.html')