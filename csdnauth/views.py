from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    """用户登录接口"""
    return render(request,'login.html')

def regist(request):
    """
    用户注册接口
    """
    return render(request,'regist.html')

def logout(request):
    """
    用户登出接口
    """
    return HttpResponse("logout")
    # return render(request,'logout.html')