# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.all() # QuerySet을 가져왔으나 아직 DB에 적용되지는 않는다. 왜냐? 접근하지 않았기 때문.

    q = request.GET.get('q', '')
    if q:       # 쿼리가 있으면
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html',{
        'post_list' : qs,
        'q' : q
    })


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {
        'post' : post
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()      # Model Form에 내재되어 있는 save 메서드 사용
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
            return redirect(post)   # post.get_absolute_url() => post_detail
    else:
        form = PostForm(instance=post)
    return render(request,'blog/post_form.html',{
        'form' : form,
    })