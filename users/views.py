from django.shortcuts import render
from use_ckeditor.models import *
from  django.contrib.auth import authenticate,login
# Create your views here.
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