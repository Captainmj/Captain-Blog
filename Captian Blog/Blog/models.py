#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Categroy(models.Model):
	'''文章分类'''
	theme = models.CharField('文章分类',max_length=10)
	created = models.DateTimeField('创建时间',auto_now_add=True)

	class Meta:
		ordering =('-created',)
		verbose_name_plural = '文章分类'

	def __str__(self):
		return self.theme


class Article(models.Model):
	'''标题'''
	categroy = models.ForeignKey(Categroy,verbose_name='分类', on_delete=models.CASCADE)
	STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('personal','Personal'),
    )
	title = models.CharField('标题',max_length=70)
	created = models.DateTimeField('创建时间', auto_now_add=True)
	updated = models.DateTimeField('更新时间', auto_now=True)
	status = models.CharField('文章状态', max_length=10, choices=STATUS_CHOICES, default='draft')
	author = models.ForeignKey(User,verbose_name='作者')
	slug = models.SlugField('标签', max_length=250, unique_for_date='created')
	body = models.TextField('正文')
	topped = models.BooleanField('置顶', default=False)
	views = models.PositiveIntegerField('浏览量', default=0)
	likes = models.PositiveIntegerField('点赞数', default=0)
	abstract = models.CharField('摘要', max_length=7, blank=True, null=True,
                                help_text="可选，如若为空将摘取正文的前54个字符")
	#此功能暂时无法实现


	class Meta:
		ordering = ('-created',)
		verbose_name_plural = '文章'
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('Blog:detail', kwargs={'pk': self.pk})


class Comments(models.Model):
	'''评论管理'''
	article = models.ForeignKey(Article, verbose_name='文章评论',related_name='comments')
	comment_body = models.TextField('评论内容')
	comment_time = models.DateTimeField('评论时间',auto_now=True)
	name = models.CharField('昵称',max_length=10)
	active = models.BooleanField(default=True)
	#comment_response = models.TextField('评论回复')
	#comment_like = models.PositiveIntegerField('点赞数', default=0)

	class Meta:
		ordering = ('comment_time',)
		verbose_name_plural = '评论管理'

	def __str__(self):
		 return 'Comment by {} on {}'.format(self.name, self.article)









