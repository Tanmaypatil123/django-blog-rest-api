from venv import create
from django.shortcuts import render
from rest_framework import generics,authentication,permissions
from .permissions import IsStaffEditorPermission
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Blog
from .serializers import BlogSerializers
from rest_framework.response import Response
from rest_framework import mixins
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
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content =content)

blog_create_list_view = BlogCreateListAPIView.as_view()        

@api_view(["GET","POST"])
def blog_all_view(request,pk=None,*args,**kwargs):
    method = request.method

    if method =="GET":
        if pk is not None:
            obj = get_object_or_404(Blog,pk=pk)
            data = BlogSerializers(obj,many=False)
            return Response(data)
        queryset = Blog.objects.all()
        data = BlogSerializers(queryset,many=True).data
        return Response(data)

    if method == "POST":
        serializer = BlogSerializers(data = request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None   
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)     

class BlogUpdateAPIView(generics.UpdateAPIView):
    queryset = Blog.objects.all()  
    serializer_class =BlogSerializers
    lookup_field = 'pk'

    def perform_update(self,serializer):
        instance = serializer.save() 
        if not instance.content:
            instance.content = instance.title 

blog_update_view = BlogUpdateAPIView.as_view()


class BlogDeleteAPIView(generics.DestroyAPIView):
    queryset = Blog.objects.all()  
    serializer_class =BlogSerializers
    lookup_field = 'pk'

    def perform_delete(self,instance):
        super().perform_destroy(instance)


blog_delete_api_view = BlogDeleteAPIView.as_view()  


class BlogMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = 'pk'

    def get(self,request,*args,**kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)   

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self,serializer):         
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)    

blog_mixins_view = BlogMixinView.as_view()
