# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-23 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20170420_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_like',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comment_response',
        ),
        migrations.AddField(
            model_name='comments',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default=1, max_length=10, verbose_name='昵称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Blog.Article', verbose_name='文章评论'),
        ),
    ]
