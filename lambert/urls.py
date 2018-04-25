"""lambert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url,re_path
from django.views.static import serve
from lambert.settings import MEDIA_ROOT
from use_ckeditor.views import *
from users.views import LoginView,RegisterView
from markdown.views import MarkdownInfo

import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage,name="index"),
    path('login/',LoginView.as_view(), name="login"),
    path('register/',RegisterView.as_view(), name="register"),
    path('articalPage/<int:artical_id>/', ArticleInfo, name="rich_page"),
    path(r'markdownPage/<int:artical_id>/', MarkdownInfo,name="markdown_page"),
    path(r'xadmin/', xadmin.site.urls),
    re_path('image_upload/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^captcha/', include('captcha.urls')),
]
