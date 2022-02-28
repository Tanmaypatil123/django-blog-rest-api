from django import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import views
urlpatterns = [
    path('auth/',obtain_auth_token),
    path('',views.api_home)
]