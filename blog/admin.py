from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog,BlogComment,BlogTopicCategory

class BlogTopicCategoryAdmin(admin.ModelAdmin):
    list_display=['name']

class BlogAdmin(admin.ModelAdmin):
    list_display=['title','content','pub_time','category_id','author']

class BlogCommentAdmin(admin.ModelAdmin):
    list_display=['content','pub_time','blog','author']

admin.site.register(BlogTopicCategory,BlogTopicCategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)
