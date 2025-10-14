from django.db import models
from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class CaptchaModels(models.Model):
    """
    邮箱验证码模型
    """
    email=models.EmailField()
    captcha_code=models.CharField(max_length=6)
    create_time=models.DateTimeField(auto_now_add=True)

class RegistForms(forms.Form):
    """
    注册表单
    """
    username=forms.CharField(max_length=10,min_length=2,error_messages={'required':'用户名不能为空!','min_length':'用户名长度不能小于2位!','max_length':'用户名长度不能大于10位!'})
    email=forms.EmailField(max_length=100,error_messages={'required':'邮箱不能为空!','invalid':'邮箱格式错误!'})
    password=forms.CharField(max_length=20,min_length=8,error_messages={'required':'密码不能为空!','min_length':'密码长度不能小于8位!','max_length':'密码长度不能大于20位!'})
    captcha=forms.CharField(max_length=6,min_length=6,error_messages={'required':'验证码不能为空!','max_length':'验证码长度不能大于6位!','min_length':'验证码长度不能小于6位!'})

    def clean_email(self):
        email=self.cleaned_data.get('email')
        exists=User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('邮箱已注册!')
        return email
    

    def clean_captcha(self):
        captcha=self.cleaned_data.get('captcha')
        email=self.cleaned_data.get('email')
        exisits=CaptchaModels.objects.filter(email=email,captcha_code=captcha).first()
        if not exisits:
            raise forms.ValidationError('验证码错误!')
        return captcha
        

