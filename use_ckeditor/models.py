# coding:utf-8
from django.template.defaultfilters import slugify
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    name = models.CharField("标签名",max_length=128, unique=True)
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题', max_length=256)
    content = RichTextUploadingField('内容')
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)
    tag   = models.ManyToManyField(Category,blank=True,verbose_name = '标签名')

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title

class Web_link(models.Model):
    name = models.CharField('网站名称', max_length=256)
    address = models.URLField('URL',max_length = 256)

    class Meta:
        verbose_name = "常用站点"
        verbose_name_plural = "常用站点"

    def __str__(self):
        return self.name