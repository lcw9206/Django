# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # default : "/accounts/login/"
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })


# decorator
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
