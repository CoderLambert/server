
import  xadmin
from .models import Article, Category, Web_link

@xadmin.sites.register(Article)
class AdminArticle(object):
    list_display = ('title', 'original', 'auther', 'update_time')
    fields = ('title','auther','original','link_address','content','tag')

#xadmin.site.register(AdminArticle,Article)
xadmin.site.register(Category)
xadmin.site.register(Web_link)
