from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
    obj={
        "name":"rafiul islam",
        "age":25,
        "department":"Computer Science and  Engineering",
        "University":"Islamic University, Kushtia",
        "description":"Kushtia National Highway which provides its lifeline of connectivity with the rest of the country.",
        "Skills":['c','c++',"python","javaScript","Express","Node","Mysql","MongoDB"],
        'date':datetime.datetime.now(),
        'lst':[
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 40},
    {'name': 'Joe', 'age': 31},
]
    }

    return  render(request,'home.html',context=obj)