from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('blog/<int:blog_id>',views.blog_detail,name='blog_detail'),
    path('blog/publish/',views.publish_blog,name='publish_blog'),
]
