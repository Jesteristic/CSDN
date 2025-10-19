from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('blog/<int:blog_id>',views.blog_detail,name='blog_detail'),
    path('blog/publish_blog',views.pub_blog,name='publish_blog'),
    path('blog/publish_comment',views.pub_comment,name='publish_comment'),
    path('blog/search_blogs',views.search_blogs,name='search_blogs'),
]
