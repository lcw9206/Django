from django.contrib import admin
from .models import Post


# Register your models here.

# admin.site.register(Post)

# 등록법 2
'''
class PostAdmin(admin.ModelAdmin):  # 이 형태는 커스터 마이징이 가능하다.
    list_display = ['id', 'title', 'created_at', 'updated_at']
admin.site.register(Post, PostAdmin) # 참고: 같은 모델 중복 등록은 불가 
'''

@admin.register(Post)   # 등록법 3 : 장식자 형태로 지원
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']
    actions = ['make_published']


    def make_published(self, request, queryset):      # 함수 기반 액션 생성하기
        updated_count = queryset.update(status='p')
        self.message_user(request, '{} sucessfully marked as published'.format(updated_count))
    make_published.short_description = 'Mark selected stories as published'


    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description = '글자수'