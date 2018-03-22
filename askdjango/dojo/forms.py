#dojo/forms.py

from django import forms

def min_length_3_validators(value):
    if(len(value) < 3):
        raise forms.ValidationError('3글자 이상 입력해주세요.')

class PostForm(forms.Form):
    ''' 
    models의 content는 DB에 길이제한이 없는 문자열의 형태를 넣기위해 Textarea로 선언했다.
    하지만 forms는 DB와 관련이 없기에 문자열을 나타내는 CharField를 title과 동일하게 선언하고, 
    한줄위젯이 아닌 여러줄 위젯을 사용하기위해 widget=forms.Textarea로 선언했다.
    '''
    title = forms.CharField(validators=min_length_3_validators)
    content = forms.CharField(widget=forms.Textarea)

