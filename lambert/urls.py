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

from users.views import LoginView,user_logout,RegisterView,UserActiveView
from use_ckeditor.views import HomePage,ArticleInfo, ArticleTag, Artical_time_year, Artical_time_year_month
from markdown.views import Markdown, MarkdownInfo, MarkdownTag,Markdown_time_year,Markdown_time_year_month

import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(), name="login"),
    path('logout/', user_logout, name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('active/<slug:activecode>/', UserActiveView.as_view(), name="user_active"),

    path('', HomePage, name="index"),
    path('<int:artical_tag>/', ArticleTag, name="ArticleTag"),
    path('time/<int:artical_year>/', Artical_time_year, name="Artical_time_year"),
    path('time/<int:artical_year>/<int:artical_month>', Artical_time_year_month, name="Artical_time_year_month"),

    path('articalPage/<int:artical_id>/', ArticleInfo, name="rich_page"),

    path('markdown/', Markdown, name ="markdown_index"),
    path(r'markdown/<int:markdownTag_id>/', MarkdownTag, name="MarkdownTag"),
    path('markdown/time/<int:artical_year>/', Markdown_time_year, name="Markdown_time_year"),
    path('markdown/time/<int:artical_year>/<int:artical_month>', Markdown_time_year_month, name="Markdown_time_year_month"),
    path(r'markdownPage/<int:artical_id>/', MarkdownInfo,name="markdown_page"),

    path(r'xadmin/', xadmin.site.urls),

    re_path('image_upload/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^captcha/', include('captcha.urls')),
]
