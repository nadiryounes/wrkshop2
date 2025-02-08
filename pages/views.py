from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePageView(httpRequest):
    return HttpResponse('Hello, World!')