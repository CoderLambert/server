import  xadmin
from .models import *
from markdown.widgets import XAdminMarkdownWidget
# Register your models here.


class TestAdmin(object):
    formfield_overrides = {
        EditorMarkdownField: {'widget': XAdminMarkdownWidget()},
    }

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Markdown"
        verbose_name_plural = "Markdown"
xadmin.site.register( markdownArtical, TestAdmin)