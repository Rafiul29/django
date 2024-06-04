from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from posts.models import  Post

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
        return redirect('profile')
      else:
        messages.warning(request, 'Login informtion incorrect')
        return redirect('register')
     
  else:
    login_form=AuthenticationForm()
  return render(request,'forms.html',{'form':login_form,'type':"Login"})

@login_required
def profile(request): 
  data=Post.objects.filter(author=request.user) #filter post author 
  return render(request,'profile.html',{'data':data})

@login_required
def edit_profile(request): 
  if request.method=='POST':
    profile_form=forms.ChnageUserForm(request.POST,instance=request.user)
    if profile_form.is_valid():
      print(profile_form.cleaned_data)
      profile_form.save()
      messages.success(request, 'Profile updated in Successfully')
      return redirect("profile")
  else:
    profile_form=forms.ChnageUserForm(instance=request.user)
  return render(request,'edit_profile.html',{'form':profile_form})


def pass_chnage(request):
  if request.method=='POST':
    form=PasswordChangeForm(request.user,data=request.POST)
    if form.is_valid():

      print(form.cleaned_data)
      form.save()
      messages.success(request, 'pass change  Successfully')
      update_session_auth_hash(request,form.user)
      return redirect("profile")
  else:
    form=PasswordChangeForm(user=request.user)
  return render(request,'pass_change.html',{'form':form})