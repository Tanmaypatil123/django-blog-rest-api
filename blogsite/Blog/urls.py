from django.urls import path
from . import views
urlpatterns = [
    path("<int:pk>/",views.blog_detail_view)
]