from pyexpat import model
from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "content",
            "likes",
            "published_date"
        ]