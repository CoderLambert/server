import  xadmin
from .models import *
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile)
xadmin.site.register(Banner)
xadmin.site.register(EmailVerifyRecord)