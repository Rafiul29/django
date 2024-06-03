from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
def register(request):
  if request.method=='POST':
    register_form=forms.RegistrationForm(request.POST)
    if register_form.is_valid():
      print(register_form.cleaned_data)
      register_form.save()
      return redirect("register")
  else:
    register_form=forms.RegistrationForm()
  return render(request,'forms.html',{'form':register_form,'type':"Register"})


def user_login(request):
  if request.method=='POST':
    login_form=AuthenticationForm(request,data=request.POST)
    if login_form.is_valid():
      user_name=login_form.cleaned_data['username']
      user_pass=login_form.cleaned_data['password']
      user=authenticate(username=user_name,password=user_pass)
      if user is not None:
        messages.success(request, 'Logged in Successfully')
        login(request,user)
        return redirect('login')
      else:
        messages.warning(request, 'Login informtion incorrect')
        return redirect('register')
     
  else:
    login_form=AuthenticationForm()
  return render(request,'forms.html',{'form':login_form,'type':"Login"})



