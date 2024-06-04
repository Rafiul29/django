from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_post(request):
  if request.method=='POST':
    post_form=forms.PostForm(request.POST)
    if post_form.is_valid():
      # print(post_form.cleaned_data)
      post_form.instance.author=request.user
      post_form.save()
      return redirect("homepage")
  else:
    post_form=forms.PostForm()
  return render(request,'add_post.html',{'form':post_form})


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


def delete_post(request,id):
  form=models.Post.objects.get(pk=id).delete()
  return redirect('homepage')