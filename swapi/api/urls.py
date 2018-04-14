from django.contrib import admin
from django.urls import path, include

from api import views


urlpatterns = [
    path('people/1/', views.single_people),
    path('people/', views.list_people),
]
