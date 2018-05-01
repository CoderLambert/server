import  xadmin
from .models import *
from markdown.widgets import XAdminMarkdownWidget
# Register your models here.


class TestAdmin(object):
    formfield_overrides = {
        EditorMarkdownField: {'widget': XAdminMarkdownWidget()},
    }

    list_display = ('title', 'original', 'auther', 'update_time')
    fields = ('title','auther','original','link_address','markdown_text','tag')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Markdown"
        verbose_name_plural = "Markdown"


xadmin.site.register( markdownArtical, TestAdmin)