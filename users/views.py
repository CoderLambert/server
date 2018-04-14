from django.shortcuts import render
from  django.contrib.auth import authenticate,login
# Create your views here.
def Userlogin(request):
   if  request.method =='POST':
       user_name = request.POST.get("user_name","")
       pass_word = request.POST.get("user_password","")
       user = authenticate(username=user_name,password=pass_word)
       if user is not None:
           login(request,user)
       return render(request, 'login.html', {})

   elif request.method == "GET":
       return render(request,'login.html',{})