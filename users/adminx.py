import  xadmin
from .models import *
from django.contrib import admin
from .models import *
from markdown.widgets import AdminMarkdownWidget



# Register your models here.
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile)
xadmin.site.register(Banner)
xadmin.site.register(EmailVerifyRecord)

