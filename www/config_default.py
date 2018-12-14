#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" app """

__author__ = 'Aymer Zhang'  # 模块作者 当公开代码的时候别人就会看到了作者的大名了

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        # 'password': '123456',  # 服务器
        'password': 'password',  # 本地
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}
