import  xadmin
from .models import *
from markdown.widgets import XAdminMarkdownWidget
# Register your models here.


class TestAdmin(object):
    formfield_overrides = {
        EditorMarkdownField: {'widget': XAdminMarkdownWidget()},
    }

    list_display = ('title', 'original', 'auther', 'update_time')
    search_fields = ('title', 'original', 'auther', 'update_time') #要查询的列
    list_filter = ('title', 'original', 'update_time','markdown_text','tag') #要筛选的列
    fields = ('title','auther','original','link_address','markdown_text','tag')



xadmin.site.register( markdownArtical, TestAdmin)