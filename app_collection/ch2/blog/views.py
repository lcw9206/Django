# blog/views.py

# 클래스형 제네릭 뷰 임포트
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from .models import Post                # 테이블 조회를 위한 Post 모델 클래스 임포
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
# Create your views here.

class PostLV(ListView) :                    # ListView는 테이블에서 객체 리스트를 가져와 출력한다.
    model = Post                            # 제너릭 뷰에서 model은 가져올 테이블을 말한다.
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'           # 템플릿에 넘겨주는 객체 리스트에 대한 컨텍스트 변수 명을 posts로 지정
    paginate_by = 2                         # 한 페이지에 보여지는 객체의 수. paginate_by 속성만으로도 사용 가능

#--- DetailView
class PostDV(DetailView) :                  # DetailView는 테이블에서 특정 객체를 가져와 상세 정보를 출력한다.
    model = Post

#--- ArchiveView
class PostAV(ArchiveIndexView) :            # 테이블에서 객체 리스트를 가져와 날짜필드를 기준으로 최신 객체부터 정렬
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView) :            # 테이블에서 가져온 객체 리스트를 연도 기준으로 정렬.
    model = Post
    date_field = 'modify_date'
    make_object_list = True                 # True : 해당 연도에 해당하는 객체 리스트를 템플릿에 전달

class PostMAV(MonthArchiveView) :           # 월 기준 정렬
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView) :             # 연월일 기준 정렬
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView) :           # 오늘 날짜의 객체 리스트 출력
    model = Post
    date_field = 'modify_date'

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'