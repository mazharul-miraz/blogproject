from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def learn_django(request):
    return HttpResponse("<h1>Learn Django</h2>")

def learn_python(request):
    return HttpResponse("<h1>Learn python</h2>")