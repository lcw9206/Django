from django import forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=10)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post,fields='__all__')

'''
reverse는 프로젝트가 모두 임포트가 되어 초기화 상태가 되어야 수행된다.
하지만 현재 reverse는 초기화 전, import 시점에 리버싱을 실시하므로 동작하지 않는다.
따라서 이를 해결하고자 reverse_lazy를 사용해 success_url이 사용될 때, 리버싱을 실시하도록 지연시킨다.
'''
post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
