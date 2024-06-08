from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator




class UserCreateView(CreateView):
  template_name='forms.html'
  form_class = forms.RegistrationForm
  success_url = reverse_lazy('login')
  
  
class UserLoginView(LoginView):
  template_name='forms.html'
  
  def get_success_url(self):
    return reverse_lazy('profile' )
  
  def form_valid(self, form):
      return super().form_valid(form)

  def form_invalid(self, form):
      return super().form_invalid(form)
  
  def get_context_data(self, **kwargs):
    context= super().get_context_data(**kwargs)
    context['type']="Login"
    return context


# @login_required
# def profile(request): 
#   return render(request,'profile.html')

@method_decorator(login_required ,name="dispatch")
class Profile(TemplateView):
  template_name='profile.html'

def pass_chnage(request):
  if request.method=='POST':
    form=PasswordChangeForm(request.user,data=request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'pass change  Successfully')
      update_session_auth_hash(request,form.user)
      return redirect("profile")
  else:
    form=PasswordChangeForm(user=request.user)
  return render(request,'pass_change.html',{'form':form})


class UserLogoutView(LogoutView):
   def get_success_url(self):
    return reverse_lazy('login')
