from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<center>Successfull </center>')

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_markup(request):
    return HttpResponse('<h1>Hello Python</h1>')

def learn_var(request):
    a = '<h1>hello world variable<h2>'
    return HttpResponse(a)

def learn_math(request):
    a = 10+10
    return HttpResponse(a)


