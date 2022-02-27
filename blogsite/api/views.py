from django.shortcuts import render
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from rest_framework.response import Response
from Blog.serializers import BlogSerializers
from Blog.models import Blog
# Create your views here.
# @api_view(["GET"])
# def api_home(request,*args,**kwargs):
#     instance = Blog.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         #data = model_to_dict(model_data,fields=["id",'title','content','published_date'])
#         data = BlogSerializers(instance).data
#     return Response(data)     

@api_view(["POST"])
def api_home(request,*args,**kwargs):
    serializer = BlogSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)

        return Response(serializer.data)
    return Response({
        "invalid":"not good request"
    },status=400)