from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'pages/index.html') # from the pages folder in templates

def about(request):
    return render(request,'pages/about.html')