from django import forms
import datetime
from .models import ContactModel

class ContactFormAPI(forms.Form):
  name=forms.CharField(max_length=10,label="Please enter your name ",initial='your name')
  roll=forms.IntegerField(help_text = "Enter 6 digit roll number")
  password=forms.CharField(widget=forms.PasswordInput())
  email=forms.EmailField(label="Please enter your email address")
  comment=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
  aggree=forms.BooleanField(initial=True)
  birth_date=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
  BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
  birth_year=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
  day=forms.DateField(initial=datetime.date.today)

  FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
  ]
  favourite_color=forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES)
  favourite_color_mul=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)


class ContactFormModel(forms.ModelForm):
    class Meta:
       model=ContactModel
       fields="__all__"
       widgets={
      'date_field':forms.TextInput(attrs={'type':'date'}),
      'date_time_field':forms.TextInput(attrs={'type':'datetime-local'})
      }