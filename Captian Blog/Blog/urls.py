#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 详情页
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #文章归档
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.Archives, name='Archives'),
    #文章主题
    url(r'^category/(?P<pk>[0-9]+)/$', views.categroy_detail, name='category'),
    # 写文章
    url(r'^new_article/$', views.new_article, name='new_article'),
    #文章草稿箱
    url(r'^drafts/$', views.article_draft_list, name='article_draft_list'),
    #编辑文章
    url(r'^edit_article/(?P<pk>[0-9]+)/$', views.edit_article, name='edit_article'),
    #删除文章
    url(r'^article_remove/(?P<pk>[0-9]+)/$', views.article_remove, name='article_remove'),
    #全文搜索
    url(r'^search/', include('haystack.urls')),
]
