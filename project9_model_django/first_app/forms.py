from django import forms
# from first_app.models import StudentModel
from . import models

class StudentForm(forms.ModelForm):
  class Meta:
    model=models.StudentModel
    fields='__all__'
    # exclude=['roll'] #hide roll form
    labels={
      'name':"Student name",
      'roll':"Student roll"
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

