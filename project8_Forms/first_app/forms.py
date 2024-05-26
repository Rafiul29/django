from typing import Any
from django import forms
# widgets == filed to html input
# initial="rafiul"
class contactFrom(forms.Form):
  name=forms.CharField(label="User Name: ",help_text="Enter your full name",disabled=False,widget=forms.Textarea(attrs={'id':'text_area',"class":"class1 class2",'placeholder':'Enter your full name'}))
  file=forms.FileField(label="File")

  email=forms.EmailField(label="User Email")
  # age=forms.IntegerField(label="Age")
  age=forms.CharField(widget=forms.NumberInput)
  weights=forms.FloatField()
  balance=forms.DecimalField()
  gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female'),('Other','Other')])
  check=forms.BooleanField(label="Check")
  birthday=forms.DateField(widget=forms.DateInput(attrs={'type':"date"}))
  appointment=forms.CharField(widget=forms.DateInput(attrs={'type':"datetime-local"}))
  CHOICES=[('S',"Small"),("M","Medium"),("L","Large")]
  size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
  MEAL=[('P','Pepperoni'),('M',"Mashroom"),("B","Beef")]
  pizza=forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple) 

  

class StudentData(forms.Form):
  name=forms.CharField(widget=forms.TextInput)
  email=forms.EmailField(widget=forms.EmailInput)

  # def clean_name(self):
  #   valname=self.cleaned_data["name"]
  #   if len(valname) < 10:
  #     raise forms.ValidationError("Enter a name with at least 10 characters")
  #   return valname
  
  # def clean_email(self):
  #   valemail=self.cleaned_data["email"]
  #   if ".com" not in valemail:
  #     raise forms.ValidationError("Enter a valid email address")
  #   return valemail

  def clean(self):
    cleaned_data=super().clean()
    name=cleaned_data["name"]
    email=cleaned_data["email"]
    if len(name) < 10:
      raise forms.ValidationError("Enter a name with at least 10 characters")
    if ".com" not in email:
      raise forms.ValidationError("Enter a valid email address")
    return cleaned_data