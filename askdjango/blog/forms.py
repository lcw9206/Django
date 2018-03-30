from django import forms
from .models import Post
from askdjango.widgets.naver_map_point_widget import NaverMapPointWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        # widgets을 이용해 재 정의할 필드 지정
        widgets = {
            'lnglat' : NaverMapPointWidget(attrs={'width': 300, 'height': 300}),
        }

