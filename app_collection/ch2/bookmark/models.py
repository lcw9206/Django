from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)   # URLField의 첫 인자는 url 컬럼에 대한 별칭이다.

    def __str__(self):      # 객체를 문자열로 표현해 주기 위한 함수
        return self.title