from django.shortcuts import render,redirect
from . import models
from first_app.forms import StudentForm
# Create your views here.
def home(request):
  student = models.Student.objects.all()
  
  return render(request,'home.html',{'data':student})

def delete_student(request,roll):
  form=models.Student.objects.get(pk=roll).delete()
  return redirect('homepage')

  
def create(request):
  if request.method=='POST':
    form=StudentForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      print(form.cleaned_data)
      # return redirect('homepage')
  else:
    form=StudentForm()
  return render(request,'create.html',{'form':form})

