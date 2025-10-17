from django.http import JsonResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
# from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import BlogTopicCategory,Blog,BlogComment

# Create your views here.
def index(request):
    return render(request,'index.html')
def blog_detail(request,blog_id):
    return render(request,'blog_detail.html')


# @login_required(login_url=reverse('csdnauth:login')) # 由于还未在内存中未存储，失败
@login_required(login_url=reverse_lazy('csdnauth:login')) # 懒反转
def publish_blog(request):
    return render(request,'publish_blog.html')

@require_http_methods(['POST'])
# @csrf_protect
@csrf_exempt # 测试环境
def pub_blog(request):
    data=request.POST
    title=data.get('title')
    topic=data.get('topic')
    content=data.get('content')
    author=data.get('author')
    Blog.objects.create(
        title=title,
        content=content,
        category=topic,
        author=author,
    )
    return JsonResponse(
        {
            'code':200,
            'msg':'发布成功'
        }
    )
