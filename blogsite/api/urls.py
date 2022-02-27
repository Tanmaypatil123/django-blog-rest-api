from django import views
from django.urls import path
from api import views
urlpatterns = [
    path('',views.api_home)
]