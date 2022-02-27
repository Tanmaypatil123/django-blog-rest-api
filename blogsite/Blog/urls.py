from django.urls import path
from . import views
urlpatterns = [
    path("",views.blog_create_list_view),
    path("<int:pk>/",views.blog_detail_view),
]