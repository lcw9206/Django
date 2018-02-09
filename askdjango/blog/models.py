# blog/models.py

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add : 최초 저장될 때, 일시가 저장된다.
    updated_at = models.DateTimeField(auto_now=True)        # auto_now : 갱신될 때마다, 일시가 저장된다.
