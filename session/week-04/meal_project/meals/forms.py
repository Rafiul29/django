from django import forms
from .models import Food
from django.forms import ModelForm
class FoodForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(ModelForm,self).__init__(*args, **kwargs)
        # self.fields['food_name'].widget.attrs.update({'class':'form-control'})
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class':'form-control mb-3'})

    class Meta:
        model = Food
        fields = "__all__"

