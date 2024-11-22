from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mahesh(request):
    return HttpResponse('Mahesh is good at studies')

def raju(request):
    return HttpResponse('<h1>Raju goes to school everyday</h1>')

def python(request):
    return HttpResponse('<h1><marquee>Python is a high level programming language</marquee></h1>')
