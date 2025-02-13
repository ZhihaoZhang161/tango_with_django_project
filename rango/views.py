from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Rango says hello world!</h1> <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

# Create your views here.
