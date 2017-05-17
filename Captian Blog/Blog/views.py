#!/usr/bin/python
# -*- coding:utf-8 -*-
from Blog.models import Article ,Comments ,Categroy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ArticleForm, CommentForm
import markdown


def index(request):
    """
    主页信息返回
    """
    post_list = Article.objects.filter(status='published')
    return render(request, 'blog/index.html',context={'post_list': post_list})


def article_draft_list(request):
    '''文章草稿箱'''
    draft_lists = Article.objects.filter(status='draft').order_by('-created')
    context = {'draft_lists': draft_lists}
    return render(request, 'blog/article_draft_list.html', context)


def Archives(request,year,month):
    post_list = Article.objects.filter(created__year=year,
                                        created__month=month,)
    return render(request, 'blog/index.html', context= {'post_list': post_list})


def Category(request, pk):
    """
    显示对应主题所有文章
    """
    cate = get_object_or_404(Category, pk=pk)
    post_list = Categroy.objects.filter(theme=cate).filter(status='published')
    context={'post_list': post_list}
    return render(request, 'blog/index.html', context)


def categroy_detail(request, pk):
    '''分类标签文章详情'''
    article_list = Categroy.objects.get(pk=pk)
    articles = article_list.article_set.filter(status='published').order_by('-created')
    context = {'article_list': article_list,'articles': articles}

    return render(request, 'blog/categroy_detail.html', context )


def detail(request, pk):
    """
    文章详情页
    """
    article = get_object_or_404(Article, pk=pk)
    body = Article.objects.get(pk=pk)
    ''' 添加评论'''
    comments = article.comments.filter(active=True)
    #添加了一个查询集（QuerySet）来获取这个帖子所有有效的评论，通过参数过滤所有已经发布过的
    new_comment = None
    # 定义一个变量名为new_comment 及为新的评论 为 空

    if request.method == 'POST':
         # 如果是通过POST请求，我们使用提交的数据新建一条评论
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # 用is_valid()方法验证这些数据去实例化表单，如果表单通过验证，我们会做以下的操作：
            new_comment = comment_form.save(commit=False)
            '''
            通过调用表单的save()方法创建一个新的Comment对象，参数执行使对象无法立即保存到数据库中。
            注意save()方法是给ModelForm用的，而不是给Form实例用的
            '''
            new_comment.article = article
             #为刚创建的评论分配到当前的帖子
            new_comment.save()
            # 再次执行保存，这次是保存到数据库中的
    else:
        #通过GET请求被加载的，那么我们用comment_fomr = commentForm()来创建一个表单实例。
        comment_form = CommentForm()
    return render(request, 'blog/detail.html',
                    {
                    'article': article,
                    'comments': comments,
                    'body': body,
                    'comment_form': comment_form})


def new_article(request):
    '''写文章'''
    if request.method != "POST":
        form = ArticleForm()
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            #提交后跳转到index页面
            return HttpResponseRedirect(reverse('Blog:index'))
    context = {'form': form}
    return render(request, 'blog/new_article.html', context)


def edit_article(request, pk):
    '''编辑文章'''
    article = get_object_or_404(Article, pk=pk)
    body = Article.objects.get(pk=pk)

    if request.method != "POST":
        form = ArticleForm(instance=body)
    else:
        form = ArticleForm(instance=body, data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            #提交后跳转到index页面
            return HttpResponseRedirect(reverse('Blog:index'))

    context = {'article': article, 'form': form}
    return render(request, 'blog/edit_article.html', context)


def article_remove(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return HttpResponseRedirect(reverse('Blog:index'))
