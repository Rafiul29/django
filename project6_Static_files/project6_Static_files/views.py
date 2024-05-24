from django.shortcuts import render

def home(request):
  return render(request,'home.html')

# def about(request,id):
#   # print(request.GET)
#   return render(request,'about.html',{'id':id})

def about(request):
  print(request.GET)
  return render(request,'about.html',{"id":request.GET})