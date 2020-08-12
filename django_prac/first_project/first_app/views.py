from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    #요청에 대한 처리

    #응답
    return HttpResponse('Hellow, World!')

def login(request):
    return HttpResponse('로그인 되었습니다.')

def signout(request):
    return HttpResponse('잘가~')