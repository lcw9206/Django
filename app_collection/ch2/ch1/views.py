# blog/views.py

# 클래스형 제네릭 뷰 임포트
from django.views.generic.base import TemplateView  # 단순 템플릿만 보여주는 View

# Create your views here.

class HomeView(TemplateView):
    template_name = 'base.html'    # TemplateView를 사용하기 위해 필수적으로
                                   # template_name 클래스 변수를 오버라이딩으로 지정해줘야 ''=한다.
