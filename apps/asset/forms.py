#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 12:39
# @Author  : ZJJ
# @Email   : 597105373@qq.com


from django.forms import ModelForm
from django.forms import widgets as frwidgets
from .models import Host, Supplier, Manufactory, IDC


class ServerAddForm(ModelForm):
    class Meta:
        model = Host
        exclude = ['create_date', 'update_date']
        widgets = {
            'ip_managemant': frwidgets.Input(attrs={'class': 'form-control', 'placeholder': '请输入IP地址...'}),
            'ip_other1': frwidgets.Input(attrs={'class': 'form-control', 'placeholder': '请输入IP地址...'}),
            'ip_other2': frwidgets.Input(attrs={'class': 'form-control', 'placeholder': '请输入IP地址...'}),
            'os_type': frwidgets.Select(attrs={'class': 'custom-select d-block w-100'}),
            'os_release': frwidgets.Input(attrs={'class': 'form-control'}),
            'cpu_physics_count': frwidgets.Input(attrs={'class': 'form-control'}),
            'cpu_core_count': frwidgets.Input(attrs={'class': 'form-control'}),
            'cpu_logic_count': frwidgets.Input(attrs={'class': 'form-control'}),
            'mem_capacity': frwidgets.Input(attrs={'class': 'form-control'}),
            'disk_capacity': frwidgets.Input(attrs={'class': 'form-control'}),
            'raid_type': frwidgets.Select(attrs={'class': 'custom-select d-block w-100'}),
            'mac_address': frwidgets.Input(attrs={'class': 'form-control'}),
            'name': frwidgets.Input(attrs={'class': 'form-control'}),
            'sn': frwidgets.Input(attrs={'class': 'form-control'}),
            'asset_type': frwidgets.Select(attrs={'class': 'custom-select d-block w-100'}),
            'model': frwidgets.Input(attrs={'class': 'form-control'}),
            'manufactory': frwidgets.Select(attrs={'class': 'form-control'}),
            'supplier': frwidgets.Select(attrs={'class': 'form-control'}),
            'trade_date': frwidgets.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'expire_date': frwidgets.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'idc': frwidgets.Select(attrs={'class': 'form-control'}),
            'cabinet': frwidgets.Input(attrs={'class': 'form-control'}),
            'cabinet_uid': frwidgets.Input(attrs={'class': 'form-control'}),
            'memo': frwidgets.Textarea(attrs={'class': 'form-control'}),
        }


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        widgets = {
            'name': frwidgets.Input(attrs={'class': 'form-control', }),
            'tel_num': frwidgets.Input(attrs={'class': 'form-control', }),
        }
        exclude = ['create_date', 'update_date']


class ManufactoryForm(ModelForm):
    class Meta:
        model = Manufactory
        widgets = {
            'name': frwidgets.Input(attrs={'class': 'form-control', }),
            'tel_num': frwidgets.Input(attrs={'class': 'form-control', }),
        }
        exclude = ['create_date', 'update_date']

class IdcForm(ModelForm):
    class Meta:
        model = IDC
        widgets = {
            'name': frwidgets.Input(attrs={'class': 'form-control', }),
            'address': frwidgets.Input(attrs={'class': 'form-control', }),
            'area': frwidgets.Input(attrs={'class': 'form-control', }),
        }
        exclude = ['create_date', 'update_date']