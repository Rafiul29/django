from django.shortcuts import render,redirect
from .forms import AlbumForm
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_album(request):
  if request.method=='POST':
    album_form =AlbumForm(request.POST)
    if album_form.is_valid():
      # print(album_form.cleaned_data)
      album_form.save()
      return redirect('homepage')
  else:
    album_form =AlbumForm()
  return render(request,'add_album.html',{'form':album_form})

@login_required
def edit_album(request,id):
  album=models.Album.objects.get(pk=id)
  album_form=AlbumForm(instance=album)
  if request.method=='POST':
    album_form =AlbumForm(request.POST,instance=album)
    if album_form.is_valid():
      album_form.save()
      return redirect("homepage")
  return render(request,'add_album.html',{'form':album_form})

@login_required
def delete_album(request,id):
  form=models.Album.objects.get(pk=id).delete()
  return redirect('homepage')