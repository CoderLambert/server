#-*- coding:utf-8 -*-
import os
import time
import json
from django.db.models import Q
from django.http import Http404
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import markdownArtical
from use_ckeditor.models import Web_link
from markdown import settings as markdown_settings
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Markdown(request):
    if request.method == 'POST':
        key_word = request.POST.get("keyword","")
        #dic = {'title__icontains':key_word,'content__icontains':key_word}
        all_articals = markdownArtical.objects.filter(Q(title__icontains=key_word) | Q(markdown_text__icontains=key_word))
    else:
        all_articals = markdownArtical.objects.all()

    artical_nums = all_articals.count()
    web_list = Web_link.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_articals, per_page=5, request=request)
    articals = p.page(page)
    return render(request, 'markdown_index.html',
        {
        'all_articals':articals,
        'artical_nums':artical_nums,
        'web_list':web_list
        }
                  )


    # try:
    #     articleInfo = markdownArtical.objects.all(pk=artical_id)   #当 get 取不到值的时候会出现 DoesNotExist 异常，所以要保护一下
    #     #print (articleInfo[1].artical_html)
    #     return  render(request,"markdown_page.html",{'articleInfo':articleInfo})
    # except:
    #     return render(request, "error.html")


def MarkdownInfo(request,artical_id):
    try:
        articleInfo = markdownArtical.objects.get(pk=artical_id)   #当 get 取不到值的时候会出现 DoesNotExist 异常，所以要保护一下
        #print (articleInfo[1].artical_html)
        return  render(request,"markdown_page.html",{'articleInfo':articleInfo})
    except:
        return render(request, "error.html")

@csrf_exempt
def upload_image(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("editormd-image-file", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse(json.dumps({'success':0,'message':'upload image failed'}, ensure_ascii=False), content_type="application/json")
        media_root=markdown_settings.MEDIA_ROOT
        strs=myFile.name.split('.')
        suffix=strs[-1]
        file_name=strs[0]
        if not suffix  or suffix not in markdown_settings.MARKDOWN_IMAGE_FORMATS:
            return HttpResponse(json.dumps({'success': 0, 'message': 'upload image failed'}, ensure_ascii=False),
                                content_type="application/json")
        now_time=str(int(time.time()*1000))
        file_name = file_name.replace('(', '[').replace(')', ']')
        image_floder=os.path.join(media_root,markdown_settings.MARKDOWN_IMAGE_FLODER)
        if not os.path.exists(image_floder):
            os.makedirs(image_floder)
        image_name=file_name+"_"+now_time+"."+suffix
        count=1
        while os.path.exists(os.path.join(image_floder,image_name)):
            image_name = file_name + "_" + now_time + "["+str(count)+"]." + suffix
            count+=1
        destination = open(os.path.join(image_floder, image_name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse(json.dumps({'success':1,'message':'upload image successed','url':markdown_settings.MEDIA_URL+markdown_settings.MARKDOWN_IMAGE_FLODER+"/"+image_name}, ensure_ascii=False), content_type="application/json")