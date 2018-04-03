from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # Meta를 상속받아 fields만 재정의
        fields = UserCreationForm.Meta.fields + ('email', 'phone')