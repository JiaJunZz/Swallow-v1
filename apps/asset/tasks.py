#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 16:23
# @Author  : ZJJ
# @Email   : 597105373@qq.com
from __future__ import absolute_import, unicode_literals
from celery import task
from Swallow import celery_app
from celery import shared_task
from plugin.ansible_api import Ansible_Play
import time
from multiprocessing import current_process


@celery_app.task
def get_info_ansible(ip_managemant,module,m_args=''):
    #ip_managemant,module, module_args
    current_process()._config = {'semprefix': '/mp'}

    ansible = Ansible_Play('/etc/ansible/hosts')
    ansible.run_Adhoc(ip_managemant,module,m_args)
    result = ansible.get_result()
    return result

