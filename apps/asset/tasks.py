#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 16:23
# @Author  : ZJJ
# @Email   : 597105373@qq.com
from __future__ import absolute_import, unicode_literals
from celery import task
from Swallow import celery_app
from celery import shared_task

import time


@celery_app.task
def sendmail(email):
    print('start send email to %s' % email)
    time.sleep(5) #休息5秒
    print('success')
    return True
