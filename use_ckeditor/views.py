from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import *
from django.http import Http404
from django.db.models.aggregates import Count
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def HomePage(request):
    if request.method == 'POST':
        key_word = request.POST.get("keyword","")
        #dic = {'title__icontains':key_word,'content__icontains':key_word}
        all_articals = Article.objects.filter(Q(title__icontains=key_word) | Q(text__icontains=key_word)).order_by('tag')
    else:
        all_articals = Article.objects.all().order_by('-update_time')

    artical_nums = all_articals.count()
    web_list = Web_link.objects.all().order_by('web_tag')
    friend_link_list = FriendLink.objects.all()

    dates = Article.objects.datetimes('pub_date', 'month', order='DESC')
    category_list = Category.objects.annotate(num_Articles=Count('article')).filter(num_Articles__gt=0).order_by("name")

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_articals, per_page=5, request=request)
    articals = p.page(page)

    return render(request, 'index.html',
        {
        'dates': dates,
        'web_list': web_list,
		'friend_link_list':friend_link_list,
        'all_articals':articals,
        'artical_nums':artical_nums,
        'category_list': category_list,
        }
    )

def ArticleTag(request,artical_tag):
    if request.method == 'POST':
        key_word = request.POST.get("keyword","")
        #dic = {'title__icontains':key_word,'content__icontains':key_word}
        all_articals = Article.objects.filter(tag=artical_tag).filter(Q(title__icontains=key_word) | Q(text__icontains=key_word)).order_by('tag')
    else:
        all_articals = Article.objects.filter(tag=artical_tag).order_by('-update_time')

    artical_nums = all_articals.count()
    web_list = Web_link.objects.all().order_by('web_tag')
    friend_link_list = FriendLink.objects.all()

    dates = Article.objects.datetimes('pub_date', 'month', order='DESC')
    category_list = Category.objects.annotate(num_Articles=Count('article')).filter(num_Articles__gt=0).order_by("name")

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_articals, per_page=5, request=request)
    articals = p.page(page)

    return render(request, 'index.html',
        {
        'dates': dates,
        'web_list': web_list,
		'friend_link_list':friend_link_list,
        'all_articals':articals,
        'artical_nums':artical_nums,
        'category_list': category_list,
        }
    )


def Artical_time_year(request,artical_year):
    if request.method == 'POST':
        key_word = request.POST.get("keyword","")
        #dic = {'title__icontains':key_word,'content__icontains':key_word}
        all_articals = Article.objects.filter(pub_date__year = artical_year ).filter(Q(title__icontains=key_word) | Q(text__icontains=key_word)).order_by('tag')
    else:
        all_articals = Article.objects.filter(pub_date__year = artical_year ).order_by('-update_time')

    artical_nums = all_articals.count()
    web_list = Web_link.objects.all().order_by('web_tag')
    friend_link_list = FriendLink.objects.all()

    dates = Article.objects.datetimes('pub_date', 'month', order='DESC')
    category_list = Category.objects.annotate(num_Articles=Count('article')).filter(num_Articles__gt=0).order_by("name")

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_articals, per_page=5, request=request)
    articals = p.page(page)

    return render(request, 'index.html',
        {
        'dates': dates,
        'web_list': web_list,
		'friend_link_list':friend_link_list,
        'all_articals':articals,
        'artical_nums':artical_nums,
        'category_list': category_list,
        }
    )

def Artical_time_year_month(request,artical_year,artical_month):
    if request.method == 'POST':
        key_word = request.POST.get("keyword","")
        #dic = {'title__icontains':key_word,'content__icontains':key_word}
        all_articals = Article.objects.filter(pub_date__year = artical_year,pub_date__month = artical_month ).filter(Q(title__icontains=key_word) | Q(text__icontains=key_word)).order_by('tag')
    else:
        all_articals = Article.objects.filter(pub_date__year = artical_year,pub_date__month = artical_month ).order_by('-update_time')

    artical_nums = all_articals.count()
    web_list = Web_link.objects.all().order_by('web_tag')
    friend_link_list = FriendLink.objects.all()

    dates = Article.objects.datetimes('pub_date', 'month', order='DESC')
    category_list = Category.objects.annotate(num_Articles=Count('article')).filter(num_Articles__gt=0).order_by("name")

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_articals, per_page=5, request=request)
    articals = p.page(page)

    return render(request, 'index.html',
        {
        'dates': dates,
        'web_list': web_list,
		'friend_link_list':friend_link_list,
        'all_articals':articals,
        'artical_nums':artical_nums,
        'category_list': category_list,
        }
    )


def ArticleInfo(request,artical_id):
    try:
        print(artical_id)
        articleInfo = Article.objects.get(pk=artical_id)   #当 get 取不到值的时候会出现 DoesNotExist 异常，所以要保护一下
        web_list = Web_link.objects.all()
        friend_link_list = FriendLink.objects.all()

        return  render(request,"artical_page.html",{
		'articleInfo':articleInfo,
		'web_list':web_list,
		'friend_link_list':friend_link_list
		})
    except:
        return render(request, "error.html")
