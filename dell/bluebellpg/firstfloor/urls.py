from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('show_time/',views.show_time),
]

    