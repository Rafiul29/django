from django.shortcuts import render,redirect
from .forms import AlbumForm
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


@method_decorator(login_required ,name="dispatch")
class AddAlbumCreateView(CreateView):
  model=models.Album
  form_class=AlbumForm
  template_name='add_album.html'
  success_url = reverse_lazy('homepage')
  
  def form_valid(self,form):
      return super().form_valid(form)


@method_decorator(login_required ,name="dispatch")
class EditAlbumView(UpdateView):
  model=models.Album
  form_class=AlbumForm
  template_name='add_album.html'
  pk_url_kwarg='id'
  success_url = reverse_lazy('homepage')


@method_decorator(login_required ,name="dispatch")
class DeleteAlbumView(DeleteView):
  model=models.Album
  pk_url_kwarg='id'
  template_name='delete.html'
  success_url = reverse_lazy('homepage')
