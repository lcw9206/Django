from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    qs = Post.objects.all() # QuerySet을 가져왔으나 아직 DB에 적용되지는 않는다. 왜냐? 접근하지 않았기 때문.

    q = request.GET.get('q', '')
    if q:       # 쿼리가 있으면
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html',{
        'post_list' : qs,
        'q' : q
    })
