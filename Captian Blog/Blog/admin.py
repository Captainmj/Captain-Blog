#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.contrib import admin
import xadmin
from .models import Article, Categroy, Comments

class ArticleAdmin(admin.ModelAdmin):

	list_display = ('id','title','created','status','topped','abstract','categroy')


class CategroyAdmin(admin.ModelAdmin):
	list_display = ('id','theme','created')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'comment_time','active')
    #定义显示属性的内容包含的内容
    list_filter = ('active', 'comment_time')
    #list_filter属性，实现简单的过滤功能
    search_fields = ('name',  'body')
    #通过使用search_fields属性定义了一个搜索字段列

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Categroy,CategroyAdmin)
xadmin.site.register(Comments,CommentAdmin)


