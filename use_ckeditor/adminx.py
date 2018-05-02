
import  xadmin
from .models import Article, Category, Web_link

@xadmin.sites.register(Article)
class AdminArticle(object):
    list_display = ('title', 'original', 'auther', 'update_time')
    search_fields = ('title', 'original', 'auther', 'update_time') #要查询的列
    list_filter = ('title', 'original', 'update_time','content','tag') #要筛选的列
    fields = ('title','original','link_address','content','tag')

#xadmin.site.register(AdminArticle,Article)
xadmin.site.register(Category)
xadmin.site.register(Web_link)
