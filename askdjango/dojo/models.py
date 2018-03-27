# dojo/models.py

from django.db import models
from django.core.validators import MinLengthValidator
from django import forms

'''
기존 form에서 유효성을 체크할 때와 달리, model에서는 입력뿐만 아니라 
admin페이지에서도 유효성이 체크되는 것을 볼 수 있다.
이것은 admin도 model을 통해 자체적으로 model Form을 생성하기 때문이다.
'''


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    user_agent = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                    choices = (
                                        ('A', 'A서버'),
                                        ('B', 'B서버'),
                                        ('C', 'C서버'),
                                    ))
    user_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])

    class Meta:
        unique_together = [
            ('server_name', 'user_name'),
        ]
