from django.contrib import admin
from .models import Post


# Register your models here.

admin.site.register(Post)

# 등록법 2
'''
class PostAdmin(admin.ModelAdmin):  # 이 형태는 커스터 마이징이 가능하다.
    list_display = ['id', 'title', 'created_at', 'updated_at']
admin.site.register(Post, PostAdmin) # 참고: 같은 모델 중복 등록은 불가 
'''
'''
@admin.register(Post)   # 등록법 3 : 장식자 형태로 지원
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
'''