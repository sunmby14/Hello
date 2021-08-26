from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def adesunbo(request):
    return HttpResponse("Hello, Adesunbo!")

def motunrade(request):
    return HttpResponse("Hello, Motunrade!")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})
