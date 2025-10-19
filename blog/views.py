from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.db.models import Q # Q表达式
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_POST,require_GET
from .models import BlogTopicCategory,Blog,BlogComment
from .forms import Pub_blog_Form

# Create your views here.
def index(request):
    blogs=Blog.objects.all()
    return render(request,'index.html',context={
        'blogs':blogs
    })

def blog_detail(request,blog_id):
    try:
        blog=Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog=None
    return render(request,'blog_detail.html',context={'blog':blog})

@require_http_methods(['POST','GET'])
# @login_required(login_url=reverse('csdnauth:login')) # 由于还未在内存中未存储，失败
@login_required(login_url=reverse_lazy('csdnauth:login')) # 懒反转
def pub_blog(request):
    if request.method=='GET':
        topic_categeries=BlogTopicCategory.objects.all()
        return render(request,'publish_blog.html',context={'topic_categeries':topic_categeries})
    else:
        form =Pub_blog_Form(request.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            content=form.cleaned_data.get('content')
            category_id=form.cleaned_data.get('category')
            category = BlogTopicCategory.objects.get(id=category_id)
            blog=Blog.objects.create(title=title,content=content,category=category,author=request.user)
            return JsonResponse(
                {
                    "code":200,
                    "msg":"发布成功",
                    "data":{
                        "blog_id":blog.id
                    }
                    
                }
            )
        else:
            return JsonResponse({
                "code":400,
                "msg":"参数错误！"
            })

@require_POST
@login_required() # 懒反转
def pub_comment(request):
    post_data=request.POST
    blog_id=post_data.get('blog_id')
    blog=Blog.objects.get(id=blog_id)
    content=post_data.get('content')
    BlogComment.objects.create(content=content,blog=blog,author=request.user)
    redirect(reverse("blog:blog_detail",kwargs={'blog_id':blog_id}))

@require_GET
def search_blogs(request):
    # /search_blogs?keywords=xxx
    key_words=request.GET.get('keywords')
    print(key_words)
    blogs=Blog.objects.filter(Q(title__icontains=key_words) | Q(content__icontains=key_words))
    return render(request,'index.html',context={
        "blogs":blogs
    })