from django.shortcuts import render
from django.http import HttpResponse
import datetime
def index(request):
    return HttpResponse("hello raju")
def date_time(request):
    time=datetime.datetime.now()
    string='the time is {}'.format(time)
    return HttpResponse(string)
def simple_view(request):
    context={'name':'nagaraju'}
    return render(request,"show_html.html",context)
def age_check(request):
    return render(request,"age_checker.html")
def display_name(request):
    context={'name':'raju'}
    return render(request, "display_name.html", context)
# Create your views here.
