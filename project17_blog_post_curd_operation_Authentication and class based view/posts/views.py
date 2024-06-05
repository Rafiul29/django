from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
# @login_required
# def add_post(request):
#   if request.method=='POST':
#     post_form=forms.PostForm(request.POST)
#     if post_form.is_valid():
#       # print(post_form.cleaned_data)
#       post_form.instance.author=request.user
#       post_form.save()
#       return redirect("homepage")
#   else:
#     post_form=forms.PostForm()
#   return render(request,'add_post.html',{'form':post_form})


# add Post using class based view
class AddPostCreateView(CreateView):
  model=models.Post
  form_class=forms.PostForm
  template_name='add_post.html'
  success_url = reverse_lazy('homepage')

  def form_valid(self,form):
      form.instance.author=self.request.user
      return super().form_valid(form)
    
  


@login_required
def edit_post(request,id):
  post=models.Post.objects.get(pk=id)
  # print(post.content)
  post_form=forms.PostForm(instance=post)
  if request.method=='POST':
    post_form=forms.PostForm(request.POST,instance=post)
    if post_form.is_valid():
      # print(post_form.cleaned_data)
      post_form.instance.author=request.user
      post_form.save()
      return redirect("profile")
  return render(request,'add_post.html',{'form':post_form})

@login_required
def delete_post(request,id):
  form=models.Post.objects.get(pk=id).delete()
  return redirect('homepage')