from django.shortcuts import render
from . forms import  contactFrom
# Create your views here.


def home(request):
  return render(request,'./first_app/home.html')

def about(request):
  # print(request.POST)
  if request.method == 'POST':
    name=request.POST.get('username')
    email=request.POST.get('useremail')
    select=request.POST.get('select')

    return render(request,'./first_app/about.html',{'name':name,'email':email,'select':select})
  else:
    return render(request,'./first_app/about.html')
  

def signup(request):
  
  # if request.method == 'POST':
  #   name=request.POST.get('username')
  #   email=request.POST.get('useremail')

  #   return render(request,'./first_app/signup.html',{'name':name,'email':email})
  # else:
  return render(request,'./first_app/signup.html')
  
# def djangoForm(request):
#   form=contactFrom(request.POST)
#   if form.is_valid():
#     print(form.cleaned_data)
    
#   return render(request,'./first_app/django_form.html',{'form':form})



def djangoForm(request):
  if request.method == 'POST':
    form=contactFrom(request.POST,request.FILES)
    if form.is_valid():
      print(form.cleaned_data)
      file=form.cleaned_data['file']
      with open("./first_app/upload/"+file.name,"wb+") as destination:
        for chunk in file.chunks():
          destination.write(chunk)
      return render(request,'./first_app/django_form.html',{'form':form})

  else:
    form=contactFrom()
    return render(request,'./first_app/django_form.html',{'form':form})