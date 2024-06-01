from django.shortcuts import render
from django.http import HttpResponse
from task.models import Task
# Create your views here.

def home(request):
  tasks=Task.objects.all()
  return render(request,'home.html',{'data':tasks})