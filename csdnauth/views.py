from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.urls import reverse
from django.views.decorators.http import require_http_methods
import random
import string
from csdnauth.models import CaptchaModels,RegistForms
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.
def login(request):
    """用户登录接口"""
    return render(request,'login.html')

@ require_http_methods(['GET','POST'])
def regist(request):
    """
    用户注册接口
    """
    if request.method == 'GET':
        return render(request,'regist.html')
    else:
        form = RegistForms(request.POST)
        if form.is_valid():
            # 通过验证，注册用户
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            User.objects.create_user(username=username,email=email,password=password)
            return redirect(reverse('csdnauth:login'))
        else:
            print(form.errors) # 打印错误信息,方便调试
            return redirect(reverse('csdnauth:regist'))
            

def send_captcha_email(request):
    """
    发送邮件接口
    """
    email=request.GET.get("email")
    captcha_code=''.join(random.choices(string.digits+string.ascii_letters,k=6))
    # 保存验证码到数据库
    obj, created=CaptchaModels.objects.update_or_create(email=email,defaults={"captcha_code":captcha_code})
    print(obj,created)
    # 发送邮件
    _=send_mail(subject="CSDN注册验证码",
                message=f"您的注册验证码是：{captcha_code}，请勿泄露",
                from_email=None
                ,recipient_list=[email])
    return JsonResponse({"code":200,"msg":"验证码发送成功"})

def logout(request):
    """
    用户登出接口
    """
    return HttpResponse("logout")
    # return render(request,'logout.html')