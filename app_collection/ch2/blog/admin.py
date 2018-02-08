from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):              # admin 페이지에 Post 클래스가 어떻게 보여질지 정의하는 클래스
    list_display = ('title', 'modify_date')     # list_display : column 명
    list_filter = ('modify_date',)              # modify_date 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
    search_fields =  ('title', 'content')       # 검색창을 만들고, 입력 문구를 title, content column에서 찾도록 함.
    prepopulated_fields = {'slug': ('title',)}  # slug 필드를 title 필드로 미리 채워지게 한다.

admin.site.register(Post,PostAdmin)             # Post와 PostAdmin 클래스를 Admin 사이트에 등록