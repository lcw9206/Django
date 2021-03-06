# dojo/views.py

from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post


'''
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request,'dojo/post_detail.html',{
        'post': post,
    })
'''


'''
# 위의 post_detail과 동일한 기능, 그러나 CBV의 as_view를 직접 구현했다.
def generate_view_fn(model):
    def view_fn(request, id):
        instance = get_object_or_404(model, id=id)
        instance_name = model._meta.model_name
        template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name)
        return render(request, template_name,{
            instance_name: instance,
        })
    return view_fn


post_detail = generate_view_fn(Post)
'''


'''
class DetailView(object):
     def __init__(self, model):
        self.model = model
     def get_object(self, *args, **kwargs):
        return get_object_or_404(self.model, id=kwargs['id'])
     def get_template_name(self):
        return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)
     def dispatch(self, request, *args, **kwargs):
        return render(request, self.get_template_name(), {
            self.model._meta.model_name: self.get_object(*args, **kwargs),
        })

     @classmethod
     def as_view(cls, model):
        def view(request, *args, **kwargs):
            self = cls(model)
            return self.dispatch(request, *args, **kwargs)
        return view


post_detail = DetailView.as_view(Post)
'''


post_detail = DetailView.as_view(model=Post)


def post_new(request):
    if request.method == 'POST':        # Post는 request, FILES를 제공받는다.
        form = PostForm(request.POST)   # 파일 업로드를 수행한 경우, request.FILES도 넣어줘야한다.
        if form.is_valid():             # is_valid()를 수행하는 시점에 form과 관련된 모든 validator들이 호출된다.
            post = form.save(commit=False)          # False로 중복되는 save를 지연시킨다.
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm()

    return render(request,'dojo/post_form.html', {
        'form' : form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else:
        form = PostForm()

    return render(request,'dojo/post_form.html', {
        'form' : form,
    })


def mysum(request, num):
    # result = sum(map(int, num.split("/")))    //와 같이 빈 문자열이 들어갔을 경우 에러 발생.
    result = sum(map(lambda s : int(s or 0), num.split('/')))       # s가 거짓일 때, or 뒤의 0의 값을 할당.
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse("안녕하세요. {}님, {}살 이시네요.".format(name, age))


def post_list1(request):
    'FBV : 직접 문자열로 html형식 응답하기'

    name='공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}입니다.</p>
    '''.format(name=name))


def post_list2(request):
    'FBV : 템플릿을 이용해 html형식 응답하기'

    name='공유'
    # render로 templates을 불러오며, 변수 name의 값을 name에 넣어 보낸다.
    response = render(request, 'dojo/post_list2.html', {'name': name})
    return response


def post_list3(request):

    return JsonResponse({
        'message' : 'Hello, Django!',
        'items' : ['Python', 'Django', 'Flask']
    }, json_dumps_params={'ensure_ascii':False})