from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello raju")

# Create your views here.
