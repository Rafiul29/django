from django.shortcuts import render,redirect
from .forms import AlbumForm
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

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

@method_decorator(login_required ,name="dispatch")
class AddAlbumCreateView(CreateView):
  model=models.Album
  form_class=AlbumForm
  template_name='add_album.html'
  success_url = reverse_lazy('homepage')

  def form_valid(self,form):
      return super().form_valid(form)
  

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