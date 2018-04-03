# accounts/urls.py

from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),

    # auth_views에 내장된 login 함수를 이용해 로그인을 처리
    url(r'^login/$', auth_views.login, name='login',
        kwargs={'template_name' : 'accounts/login_form.html'}),

    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page' : settings.LOGIN_URL}),

    url(r'^profile/$', views.profile, name='profile'),
]
