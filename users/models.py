from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from django import forms
from markdown.forms import MarkdownField,XAdminMarkdownField

# Create your models here.
class  UserProfile( AbstractUser ):
    gender_choice = (
                        ("male","男"),
                        ("female","女"),
                    )

    nick_name = models.CharField( max_length = 50, verbose_name = "昵称", default = "" )

    birthday = models.DateTimeField( verbose_name = "生日", null = True, blank = True )  # null：    如果为True，空值将会被存储为NULL，默认为False
                                                                                # blank：  如果为True，字段允许为空，默认不允许。
    gender = models.CharField( max_length=6, choices = gender_choice, default = "female",verbose_name="性别" )

    address = models.CharField( max_length = 100, default= "",verbose_name="用户地址")

    mobile  = models.CharField( max_length = 11, default= "" ,verbose_name="手机号")

    image  = models.ImageField(upload_to="images/%Y/%m", default="images/default.jpg",max_length=100, verbose_name="用户头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

#邮箱验证
class EmailVerifyRecord(models.Model):

    send_type_choice = (("register","注册"),("forgot","找回密码"))

    code = models.CharField(max_length=20,verbose_name="验证码")
    eamil =  models.EmailField(max_length=50,verbose_name="邮箱地址")
    send_type = models.CharField(choices=send_type_choice,max_length=10)
    send_time = models.DateTimeField(default = datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图")
    url   = models.URLField(max_length=200,verbose_name="访问地址")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

class BlogForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    context = XAdminMarkdownField()


class  EditorMarkdownField(models.TextField):
    pass

class markdownArtical(models.Model):
    title = models.CharField("标题",max_length=255, blank=True,default='')
    artical_html = EditorMarkdownField("内容",blank=True,default='')

    def __str__(self):
        return self.title