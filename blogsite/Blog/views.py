from django.shortcuts import render
from rest_framework import generics

from .models import Blog
from .serializers import BlogSerializers
# Create your views here.
class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

blog_detail_view = BlogDetailAPIView.as_view()    
