from time import time
from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(blank=True,null=True,max_length=500)
    likes = models.IntegerField(default=0)
    published_date = models.DateTimeField('Date published',default=timezone.now())

    def __str__(self) -> str:
        return self.title