from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import Http404

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def HomePage(request):

    all_articals = Article.objects.all()
    artical_nums = all_articals.count()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_articals, per_page=5, request=request)
    articals = p.page(page)
    return render(request, 'index.html',{
        'all_articals':articals,
    #'articals':articals,
        'artical_nums':artical_nums})

def ArticleInfo(request,artical_id):
    try:
        articleInfo = Article.objects.get(pk=artical_id)   #当 get 取不到值的时候会出现 DoesNotExist 异常，所以要保护一下
        return  render(request,"artical_page.html",{'articleInfo':articleInfo})
    except:
        return render(request, "error.html")
