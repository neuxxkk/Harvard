from django.shortcuts import render
from django.http import HttpResponse

l=[]

# Create your views here.

def index(request):
    return render(request, "test_app/index.html")

def hello(request):
    return HttpResponse("Hello, world!")

def variable(request, var):
    l.append(var)
    return render(request, 'test_app/variable.html', {
        "var":var
    })

def sub():
    print('subbmitted')

f=set(l)
print(f)
