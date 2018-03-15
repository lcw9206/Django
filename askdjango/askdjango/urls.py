# askdjango/urls.py

from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect


urlpatterns = [
    url(r'^$', lambda r: redirect('blog:post_list'), name='root'),      # redirect로 localhost:8000 접속 시, post_list로 토스
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    url(r'accounts/', include('accounts.urls', namespace='accounts')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]