from datetime import datetime

from django.db import models


from django import forms
from markdown.forms import MarkdownField,XAdminMarkdownField

# Create your models here.

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