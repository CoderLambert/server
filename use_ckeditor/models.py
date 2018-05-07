# coding:utf-8
from django.template.defaultfilters import slugify
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .reg_html2 import *


class Category(models.Model):
    name = models.CharField("标签名",max_length=128, unique=True)
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name


class Article(models.Model):
    original_choice = (
                        ("yes","是"),
                        ("no","否"),
                    )

    title = models.CharField('标题', max_length=256)
    original = models.CharField(max_length=6,choices = original_choice, default = "yes",verbose_name="是否原创")
    link_address = models.URLField(max_length=300,null=True,blank = True,verbose_name="转载地址")
    content = RichTextUploadingField('内容')
    text = models.TextField(null=True,blank = True,verbose_name="纯文本")
    auther =  models.CharField(max_length=200,null = True,blank=True,verbose_name="作者")
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)
    tag   = models.ManyToManyField(Category,blank=True,verbose_name = '标签名')

    class Meta:
        verbose_name = "文章（富文本）"
        verbose_name_plural = "文章（富文本）"

    def save(self,*args, **kwargs):
        if self.link_address is None:
            self.original = "yes"
        else:
            self.original = "no"
        self.text = get_html_text(self.content) 
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Web_type(models.Model):
    name = models.CharField("网站分类",max_length=128,null = True,blank=True, unique=True)
    class Meta:
        verbose_name = "网站分类"
        verbose_name_plural = "网站分类"

    def __str__(self):
        return self.name

class Web_link(models.Model):
    name = models.CharField('网站名称', max_length=256)
    address = models.URLField('URL',max_length = 256)
    web_tag   = models.ForeignKey(Web_type,null=True,blank=True,verbose_name = '网站分类',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "常用站点"
        verbose_name_plural = "常用站点"

    def __str__(self):
        return self.name
		
class FriendLink(models.Model):
    name = models.CharField('网站名称', max_length=256)
    address = models.URLField('URL',max_length = 256)

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = "友情链接"
