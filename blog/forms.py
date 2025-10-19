from django import forms

class Pub_blog_Form(forms.Form):
    title=forms.CharField(min_length=2,max_length=200,error_messages={'required':'标题不能为空!','min_length':'标题内容最多200字！'})
    content=forms.CharField(min_length=2,error_messages={'required':'内容不能为空'})
    category=forms.IntegerField()