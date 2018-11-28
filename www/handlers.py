#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" app """

__author__ = 'Aymer Zhang'  # 模块作者 当公开代码的时候别人就会看到了作者的大名了
import www.coreweb
import www.models
import time


@www.coreweb.get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        www.models.Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        www.models.Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        www.models.Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
