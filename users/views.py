from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from use_ckeditor.models import *
from users.models import UserProfile
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        第一步查找用户名是否存在，若存在，则继续验证密码，如果都通过，则返回user。
        有任何异常都直接返回空，一般是用户名不存在。
        同样的道理，既然可以先检查用户名是否存在来确认用户（因为用户名唯一）那么我们也可以使用email
        """
        try:
            user_obj = UserProfile.objects.get(Q(username=username) |Q(email=username))
            if user_obj.check_password(password):
                return user_obj
        except Exception as e:
            return None


def Userlogin(request):
   if  request.method =='POST':
       user_name = request.POST.get("user_name","")
       pass_word = request.POST.get("user_password","")
       user = authenticate(username=user_name,password=pass_word)
       #用户登录分两步   第一步认证通过则user是对象，否则是None
       if user is not None:
           #第二步 login，向request里面写东西，然后返回到render里面
           login(request,user)
           #正常应该返回到首页
           all_articals = Article.objects.all()
           artical_nums = all_articals.count()
           web_list = Web_link.objects.all()
           return render(request, 'index.html',
                         {
                             'all_articals': all_articals,
                             'artical_nums': artical_nums,
                             'web_list': web_list
                         }
                         )
       else:
           return render(request, 'login.html', {})
   elif request.method == "GET":
       return render(request,'login.html',{})