from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wallet(request):
    return HttpResponse("<h1>Hi!</h1>")

def users(request):
    return HttpResponse("<h1>Hi user!</h1>")