import  xadmin
from .models import Article, Category, Web_link
xadmin.site.register(Article)
xadmin.site.register(Category)
xadmin.site.register(Web_link)
