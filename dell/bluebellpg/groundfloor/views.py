from django.shortcuts import render
from django.http import HttpResponse
import datetime
def index(request):
    return HttpResponse("hello raju")
def date_time(request):
    time=datetime.datetime.now()
    string='the time is {}'.format(time)
    return HttpResponse(string)
# Create your views here.
