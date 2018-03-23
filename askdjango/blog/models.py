# blog/models.py

from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.core.urlresolvers import reverse
import re


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn')
    )
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100, verbose_name='제목',help_text='포스팅 제목을 입력해주세요. 100자 내외')
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator],blank=True, verbose_name='경도,위도', help_text='경도,위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add : 최초 저장될 때, 일시가 저장된다.
    updated_at = models.DateTimeField(auto_now=True)        # auto_now : 갱신될 때마다, 일시가 저장된다.

    class Meta:     # 기본 정렬 기준을 주기위한 선언
        ordering = ['id']

    def __str__(self):      # 쿼리셋에서 title을 얻기위한 선언
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey('Post')
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name