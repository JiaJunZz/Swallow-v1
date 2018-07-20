#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 15:20
# @Author  : ZJJ
# @Email   : 597105373@qq.com


from __future__ import absolute_import, unicode_literals

from celery import Celery
from django.conf import settings
import os
import datetime
from celery.schedules import crontab



# 获取当前文件夹名，即为该Django的项目名
# project_name = os.path.split(os.path.abspath('.'))[-1]
# project_settings = '%s.settings' % project_name

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Swallow.settings')

# 实例化Celery
app = Celery('Swallow')


# Celery加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# 使用django的settings文件配置celery
app.config_from_object('django.conf:settings')





# celery crontab
# app.conf.beat_schedule = {
#     # 每小时执行一次
#     'add-every-hour': {
#         'task': 'tasks.cron_info_ansible',
#         'schedule': crontab(minute='*/3'),
#         'args': ('hello',),
#     },
# }
#
# @app.task
# def send(message):
#     return message