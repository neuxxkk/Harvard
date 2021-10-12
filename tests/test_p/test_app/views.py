from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "test_app/index.html")

def hello(request):
    return HttpResponse("Hello, world!")

def variable(request, var):
    return render(request, 'test_app/variable.html', {
        "var":var
    })