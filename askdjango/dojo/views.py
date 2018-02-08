from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mysum(request, num):
    # result = sum(map(int, num.split("/")))    //와 같이 빈 문자열이 들어갔을 경우 에러 발생.
    result = sum(map(lambda s : int(s or 0), num.split('/')))       # s가 거짓일 때, or 뒤의 0의 값을 할당.
    return HttpResponse(result)