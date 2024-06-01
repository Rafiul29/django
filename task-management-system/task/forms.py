from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model=Task
    fields='__all__'

    labels={
      'title':"Title",
      'description':"Description",
      'date':"Assign Date",
      'is_complete':"Agree"
    }
    widgets={
      'date':forms.TextInput(attrs={'type':'date'}),
      }
    

