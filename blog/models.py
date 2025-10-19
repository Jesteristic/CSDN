from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class BlogTopicCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)  # 添加唯一约束

    class Meta:
        verbose_name='话题分类'
        verbose_name_plural=verbose_name
        
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    pub_time=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(BlogTopicCategory,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name='博客'
        verbose_name_plural=verbose_name
        ordering = ['-pub_time']  # 按发布时间倒序排列

    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    content=models.TextField()
    pub_time=models.DateTimeField(auto_now_add=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name
        ordering = ['pub_time']  # 按发布时间正序排列
    
    def __str__(self):
        return self.content

