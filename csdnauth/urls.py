from django.urls import path
from . import views

app_name='csdnauth'
urlpatterns = [
    path('login/',views.csdn_login,name='login'),
    path('regist/',views.csdn_regist,name='regist'),
    path('send_captcha_email/',views.send_captcha_email,name='send_captcha_email/'),
]
