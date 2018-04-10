# coding:utf-8
from django.template.defaultfilters import slugify
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('title', max_length=256)
    content = RichTextUploadingField('contents')
    pub_date = models.DateTimeField('express_time', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('update_time',auto_now=True, null=True)
    tag   = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Web_link(models.Model):
    name = models.CharField('name', max_length=256)
    address = models.URLField('address',max_length = 256)

    def __str__(self):
        return self.name