from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
  # dictionary  format pass data
  obj={
    'author':"rafiul",
    'name':"rafiul",
    'age':5,
    'address':"dhaka",
    'phone':"01711111111",
    'email':"rafiul.com",
    'courses':[{"id":1, "name":"cse"}, {"id":2, "name":"EE"}, {"id":3, "name":"phy"}],
    'lst':['python','is','best'],
    'birthday':datetime.datetime.now()
  }
  return render(request,'home.html',obj)
  # return render(request,'home.html',context=obj) # are samne working here