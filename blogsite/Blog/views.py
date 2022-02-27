from django.shortcuts import render
from rest_framework import generics

from .models import Blog
from .serializers import BlogSerializers
# Create your views here.
class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

blog_detail_view = BlogDetailAPIView.as_view()    


class BlogCreateAPIView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =BlogSerializers

    def create_blog(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content =content)

blog_create_view = BlogCreateAPIView.as_view() 


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class =BlogSerializers

blog_list_view = BlogListAPIView.as_view()    

class BlogCreateListAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =BlogSerializers

    def create_blog(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content =content)

blog_create_list_view = BlogCreateListAPIView.as_view()        