from django.shortcuts import render,redirect
from posts.models import Post

def home(request):
  data=Post.objects.all()
  return render(request,'home.html',{"data":data})


def delete_post(request,id):
  form=Post.objects.get(pk=id).delete()
  return redirect('homepage')

# def update_post(request,id):
#   pass
