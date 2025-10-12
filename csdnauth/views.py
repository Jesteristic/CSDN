from django.shortcuts import render

# Create your views here.
def login(request):
    """用户登录"""
    return render(request,'login.html')

def regist(request):
    """
    用户注册
    """
    return render(request,'regist.html')