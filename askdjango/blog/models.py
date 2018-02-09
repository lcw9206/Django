# blog/models.py

from django.db import models
from django.forms import ValidationError
import re
# Create your models here.

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100, verbose_name='제목',help_text='포스팅 제목을 입력해주세요. 100자 내외')
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator],blank=True, verbose_name='경도,위도', help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add : 최초 저장될 때, 일시가 저장된다.
    updated_at = models.DateTimeField(auto_now=True)        # auto_now : 갱신될 때마다, 일시가 저장된다.
