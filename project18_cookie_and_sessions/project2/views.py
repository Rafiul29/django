from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

def index(request):
  response=render(request,'index.html')
  response.set_cookie('name','rafiul',max_age=10)
  response.set_cookie('name','rafi',expires=datetime.utcnow()+timedelta(days=7))
  return response

def get_cookie(request):
  name=request.COOKIES.get('name')
  print(request.COOKIES)
  return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
 response=render(request,'delete_cookie.html')
 response.delete_cookie('name')
 return response

def set_session(request):
  data={
    'name':'rahim',
    'age':23,
    'language':'bangla'
  }
  print(request.session.get_session_cookie_age())
  print(request.session.get_expiry_date())
  request.session.update(data)

  return render(request,'index.html')


def get_session(request):
  if 'name' in request.session:
    name=request.session.get('name','Guest')
    age=request.session.get('age')
    request.session.modified=True
    return render(request,'get_session.html',{'name':name,'age':age})
  else:
    return HttpResponse('Your session has been expired')


def delete_session(request):
  # del request.session['name']
  request.session.flush()
  # request.session.clear_expired()
  return render(request,'delete_cookie.html',)