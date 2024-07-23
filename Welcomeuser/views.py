from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greetUser(request):
    return HttpResponse('Welcome Virtualization and Cloud Computing Student')
