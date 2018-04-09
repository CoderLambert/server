import  xadmin
from .models import Article, Category
xadmin.site.register(Article)
xadmin.site.register(Category)
