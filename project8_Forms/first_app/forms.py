from django import forms

class contactFrom(forms.Form):
  name=forms.CharField(label="User Name")
  file=forms.FileField(label="File")

  # email=forms.EmailField(label="User Email")
  # age=forms.IntegerField(label="Age")
  # weights=forms.FloatField()
  # balance=forms.DecimalField()
  # gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female'),('Other','Other')])
  # check=forms.BooleanField(label="Check")
  # birthday=forms.DateField()
  # appointment=forms.DateTimeField()
  # CHOICES=[('S',"Small"),("M","Medium"),("L","Large")]
  # size=forms.ChoiceField(choices=CHOICES)
  # MEAL=[('P','Pepperoni'),('M',"Mashroom"),("B","Beef")]
  # pizza=forms.MultipleChoiceField(choices=MEAL)

  