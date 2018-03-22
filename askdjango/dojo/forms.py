# dojo/forms.py

from django import forms
from .models import Post



'''
# Form을 이용
class PostForm(forms.Form):
    
    models의 content는 DB에 길이제한이 없는 문자열의 형태를 넣기위해 Textarea로 선언했다.
    하지만 forms는 DB와 관련이 없기에 문자열을 나타내는 CharField를 title과 동일하게 선언하고,
    한줄위젯이 아닌 여러줄 위젯을 사용하기위해 widget=forms.Textarea로 선언했다.
    
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    # ModelForm.save 인터페이스 흉내
    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
'''


# ModelForm을 이용, 위의 코드와 똑같은 결과가 나온다.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']   # 유저에게 입력받을 값, __all__ 설정은 전체 필드를 추가
