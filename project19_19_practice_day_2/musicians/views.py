from django.shortcuts import render,redirect
from .forms import MusicianForm
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


@method_decorator(login_required ,name="dispatch")
class AddMusicianCreateView(CreateView):
  model=models.Musician
  form_class=MusicianForm
  template_name='add_musician.html'
  success_url = reverse_lazy('add_album')
  
  def form_valid(self,form):
      return super().form_valid(form)

@method_decorator(login_required ,name="dispatch")
class EditMusicianView(UpdateView):
  model=models.Musician
  form_class=MusicianForm
  template_name='add_musician.html'
  pk_url_kwarg='id'
  success_url = reverse_lazy('homepage')