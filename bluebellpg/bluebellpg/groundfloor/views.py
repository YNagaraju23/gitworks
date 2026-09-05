from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, Geeks! Welcome to your first Django app.")
def login(request):
    return render(request,'login.html')

# Create your views here.
