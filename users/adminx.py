import  xadmin
from xadmin import views
from .models import *
from django.contrib import admin
from .models import *
from markdown.widgets import AdminMarkdownWidget
# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True
# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '25years后台管理界面'
    # 修改footer
    site_footer = 'lambert的分享平台'


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)

# Register your models here.

xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile)
xadmin.site.register(Banner)
xadmin.site.register(EmailVerifyRecord)


