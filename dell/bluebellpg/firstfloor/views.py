from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def show_time(request):
    now=datetime.now()
    return HttpResponse("this shows time  :  {}".format(now))
# Create your views here.
