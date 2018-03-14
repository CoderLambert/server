from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import Http404
# Create your views here.
def HomePage(request):
    articals = Article.objects.all()
    return render(request, 'index.html',{'articals':articals})

def ArticleInfo(request,artical_id):
    try:
        articleInfo = Article.objects.get(pk=artical_id)   #当 get 取不到值的时候会出现 DoesNotExist 异常，所以要保护一下
        return  render(request,"artical_page.html",{'articleInfo':articleInfo})
    except:
        return render(request, "error.html")
