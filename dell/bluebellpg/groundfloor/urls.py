from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('views/',views.index),
    path('date_time/',views.date_time),
    path('show_html/',views.simple_view),
    path('age_check/',views.age_check),
    path('display_name/',views.display_name),
]