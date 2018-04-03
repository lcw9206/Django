from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Profile


class SignupForm(UserCreationForm):

    phone_number = forms.CharField()

    class Meta(UserCreationForm.Meta):  # Meta를 상속받아 fields만 재정의
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 필수 필드에 생성되는 에러 생성 방지
        self.fields['username'].required= False

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            phone_number = self.cleaned_data['phone_number'])
        return user