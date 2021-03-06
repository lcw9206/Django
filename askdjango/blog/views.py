# blog/views.py

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')

    if q:       # 쿼리가 있으면
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html',{
        'post_list' : qs,
        'q' : q
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {
        'post' : post
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()      # Model Form에 내재되어 있는 save 메서드 사용
            messages.success(request, "포스팅 저장 완료!")     # 메세지 등록 코드
            return redirect(post)   # post.get_absolute_url() => post_detail
    else:
        form = PostForm()
    return render(request,'blog/post_form.html',{
        'form' : form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()      # Model Form에 내재되어 있는 save 메서드 사용
            messages.success(request, "포스팅 수정 완료!")  # 메세지 등록 코드
            return redirect(post)   # post.get_absolute_url() => post_detail
    else:
        form = PostForm(instance=post)
    return render(request,'blog/post_form.html',{
        'form' : form,
    })