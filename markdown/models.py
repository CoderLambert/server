from datetime import datetime

from django.db import models


from django import forms
from use_ckeditor.models import Category
from markdown.forms import MarkdownField,XAdminMarkdownField

# Create your models here.

class BlogForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    context = XAdminMarkdownField()

class  EditorMarkdownField(models.TextField):
    pass

class markdownArtical(models.Model):
    original_choice = (
                        ("yes","是"),
                        ("no","否"),
                    )
    title = models.CharField("标题",max_length=255, blank=True,default='')
    original = models.CharField(max_length=6,choices = original_choice, default = "yes",verbose_name="是否原创")
    link_address = models.CharField(max_length=300,null=True,blank = True,verbose_name="转载地址")
    markdown_text = EditorMarkdownField("内容",blank=True,default='')
    auther =  models.CharField(max_length=200,null = True,blank=True,verbose_name="作者")
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True,null=True)
    tag   = models.ManyToManyField(Category,blank=True,verbose_name = '标签名')
    class Meta:
        verbose_name = "文章(Markdown)"
        verbose_name_plural = "文章(Markdown)"

    def __str__(self):
        return self.title
