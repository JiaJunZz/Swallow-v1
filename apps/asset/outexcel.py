#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 10:31
# @Author  : ZJJ
# @Email   : 597105373@qq.com

import xlwt
import time
from Swallow.settings import BASE_DIR
import os


def excel_output(host):
    """
    导出excel
    """

    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet(u'资产总表',cell_overwrite_ok=True)
    row0 = [u'管理IP', u'其他IP地址1', u'其他IP地址2', u'系统类型', u'操作系统版本', u'物理CPU个数', u'CPU核数', u'逻辑CPU个数', u'内存大小(GB)'
        , u'磁盘容量(GB)', u'Raid类型', u'MAC地址', u'资产编号', u'序列号SN', u'资产类型', u'设备型号', u'制造商', u'供应商', u'购买日期', u'过保日期'
        , u'IDC机房', u'机柜', u'U位', u'备注']
    # 写入列头
    for i in range(len(row0)):
        data_sheet.write(0,i,row0[i])

    #双变量循环写入
    for c,h in list(zip(range(len(host)),host)):
        data_sheet.write(c + 1, 0, h.ip_managemant)
        data_sheet.write(c + 1, 1, h.ip_other1)
        data_sheet.write(c + 1, 2, h.ip_other2)
        data_sheet.write(c + 1, 3, h.os_type)
        data_sheet.write(c + 1, 4, h.os_release)
        data_sheet.write(c + 1, 5, h.cpu_physics_count)
        data_sheet.write(c + 1, 6, h.cpu_core_count)
        data_sheet.write(c + 1, 7, h.cpu_logic_count)
        data_sheet.write(c + 1, 8, h.mem_capacity)
        data_sheet.write(c + 1, 9, h.disk_capacity)
        data_sheet.write(c + 1, 10, h.raid_type)
        data_sheet.write(c + 1, 11, h.mac_address)
        data_sheet.write(c + 1, 12, h.sn)
        data_sheet.write(c + 1, 13, h.asset_type)
        data_sheet.write(c + 1, 14, h.model)
        data_sheet.write(c + 1, 15, str(h.manufactory))
        data_sheet.write(c + 1, 16, str(h.supplier))
        data_sheet.write(c + 1, 17, h.trade_date)
        data_sheet.write(c + 1, 18, h.expire_date)
        data_sheet.write(c + 1, 19, str(h.idc))
        data_sheet.write(c + 1, 20, h.cabinet)
        data_sheet.write(c + 1, 21, h.cabinet_uid)
        data_sheet.write(c + 1, 22, h.memo)

    filedir = os.path.join(BASE_DIR, "download")
    filename = u'资产总表' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.xls'
    file_xls = os.path.join(filedir , filename)
    print(file_xls)
    workbook.save(file_xls)

