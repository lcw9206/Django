# dojo/views.py

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


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