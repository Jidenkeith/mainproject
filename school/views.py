from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def school(request):
    return HttpResponse("This is my school app.")