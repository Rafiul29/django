from django.shortcuts import render
from .forms import ContactFormAPI,ContactFormModel


# Create your views here.
def forms_api(request):
  form=ContactFormAPI()
  return render(request,'forms_api.html',{'form':form})

def model_froms(request):
  form=ContactFormModel()
  return render(request,'model_froms.html',{'form':form})