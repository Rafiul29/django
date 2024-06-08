from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
  class Meta:
    model=Album
    fields='__all__'
    labels={
      'album_name':"Album Name",
      'musician':"Musician",
      'release_date':"Release Date",
      'rating':"Rating"
    }
    widgets={
      'release_date':forms.TextInput(attrs={'type':'date'}),
      }
    