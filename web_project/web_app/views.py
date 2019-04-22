from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'web_app/index.html')
def scooby(request):
            return render(request,'web_app/scooby.html')
def tom_jerry(request):
    return render(request,'web_app/tom_jerry.html')


# Create your views here.
