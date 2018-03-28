# dojo/admin.py

from django.contrib import admin
from .models import Post, GameUser


@admin.register(Post)   # 등록법 3 : 장식자 형태로 지원
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']
    actions = ['make_published']

    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description = '글자수'


admin.site.register(GameUser)
