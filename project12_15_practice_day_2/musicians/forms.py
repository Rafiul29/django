from django import forms
from .models import Musician


class MusicianForm(forms.ModelForm):
  class Meta:
    model=Musician
    fields='__all__'
  
    labels={
      'first_name':"First Name",
      'last_name':"Last Name",
      'phone_no':"Phone Number",
      'insurance_type':"Instance Type"
    }
    widgets={
      'name':forms.TextInput(attrs={'class':'form-control'}),
      'roll':forms.NumberInput(attrs={'class':'form-control'}),
      'father_name':forms.TextInput(attrs={'class':'form-control'}),
      'address':forms.Textarea(attrs={'class':'form-control'}),
      }
    help_texts={
      'name':"Enter student name",
      'roll':"Enter student roll",
      'father_name':"Enter student father name",
      'address':"Enter student address"
      }
    error_messages={
      'name':{
       'required':"Enter student name"
      },
      'roll':{
        'required':"Enter student roll"
      }
    }
 

