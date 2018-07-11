# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.


class Host(models.Model):
    ASSET_TYPE_CHOICES = (
        ('server', u'服务器'),
        ('virtual', u'虚拟机'),
        ('firewall', u'防火墙'),
        ('route', u'路由器'),
        ('switch', u'交换机'),
        ('other', u'其他'),
    )


    OS_TYPE = (
        ('Windows', 'Windows'),
        ('CentOS', 'CentOS'),
        ('Redhat', 'Redhat'),
        ('Ubuntu', 'Ubuntu'),
    )
    RAID_TYEP_CHOICES = (
        ('None', '无raid'),
        ('Raid0', 'Raid0'),
        ('Raid1', 'Raid1'),
        ('Raid5', 'Raid5'),
    )
    ip_managemant = models.GenericIPAddressField(verbose_name=u'管理IP', unique=True, max_length=32)
    ip_other1 = models.GenericIPAddressField(verbose_name=u'其他IP地址1', unique=True, blank=True, null=True, max_length=32)
    ip_other2 = models.GenericIPAddressField(verbose_name=u'其他IP地址2', unique=True, blank=True, null=True, max_length=32)
    os_type = models.CharField(verbose_name=u'系统类型', choices=OS_TYPE, null=True, blank=True, max_length=32)
    os_release = models.CharField(verbose_name=u'操作系统版本', null=True, blank=True, max_length=32)
    cpu_physics_count = models.SmallIntegerField(verbose_name=u'物理CPU个数', null=True, blank=True)
    cpu_core_count = models.SmallIntegerField(verbose_name=u'CPU核数', null=True, blank=True)
    cpu_logic_count = models.SmallIntegerField(verbose_name=u'逻辑CPU个数', null=True, blank=True)
    mem_capacity = models.IntegerField(verbose_name=u'内存大小(GB)', null=True, blank=True)
    disk_capacity = models.FloatField(verbose_name=u'磁盘容量(GB)', null=True, blank=True)
    raid_type = models.CharField(verbose_name=u'raid类型', null=True, blank=True, max_length=64,
                                 choices=RAID_TYEP_CHOICES, default='None')
    mac_address = models.CharField(verbose_name=u'MAC地址', max_length=64, unique=True,null=True, blank=True)
    name = models.CharField(verbose_name=u'资产编号', max_length=64, unique=True)
    sn = models.CharField(verbose_name=u'序列号SN', max_length=128, unique=True, null=True, blank=True)
    asset_type = models.CharField(choices=ASSET_TYPE_CHOICES, max_length=32, verbose_name=u'资产类型')
    model = models.CharField(verbose_name=u'设备型号', null=True, blank=True, max_length=255)
    manufactory = models.ForeignKey('Manufactory', on_delete=models.CASCADE, verbose_name=u'制造商', null=True, blank=True, max_length=32)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, verbose_name=u'供应商', null=True, blank=True, max_length=32)
    trade_date = models.DateField(verbose_name=u'购买日期', null=True, blank=True, max_length=32)
    expire_date = models.DateField(verbose_name=u'过保日期', null=True, blank=True, max_length=32)
    idc = models.ForeignKey('IDC', on_delete=models.CASCADE, verbose_name=u'IDC机房', max_length=32)
    cabinet = models.CharField(verbose_name=u'机柜', null=True, blank=True, max_length=64)
    cabinet_uid = models.CharField(verbose_name=u'u位', null=True, blank=True, max_length=64)
    memo = models.TextField(verbose_name=u'备注', null=True, blank=True, max_length=255)
    create_date = models.DateTimeField(verbose_name=u'创建时间', blank=True, null=True, auto_now_add=True, max_length=32)
    update_date = models.DateTimeField(verbose_name=u'更新时间', blank=True, null=True, auto_now=True, max_length=32)

    # admin = models.ForeignKey('UserProfile',verbose_name=u'资产管理员',max_length=32)
    # business_unit = models.ForeignKey('BusinessUnit',verbose_name=u'所属业务',max_length=50)

    class Meta:
        verbose_name = u'主机'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Manufactory(models.Model):
    name = models.CharField(verbose_name=u'厂商名称', max_length=64, unique=True)
    tel_num = models.CharField(verbose_name=u'支持电话', blank=True, null=True, max_length=32)
    create_date = models.DateTimeField(verbose_name=u'创建时间', blank=True, null=True, auto_now_add=True, max_length=32)
    update_date = models.DateTimeField(verbose_name=u'更新时间', blank=True, null=True, auto_now=True, max_length=32)

    class Meta:
        verbose_name = '制造商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(verbose_name=u'厂商名称', max_length=64, unique=True)
    tel_num = models.CharField(verbose_name=u'支持电话', blank=True, null=True, max_length=32)
    create_date = models.DateTimeField(verbose_name=u'创建时间', blank=True, null=True, auto_now_add=True, max_length=32)
    update_date = models.DateTimeField(verbose_name=u'更新时间', blank=True, null=True, auto_now=True, max_length=32)

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IDC(models.Model):
    name = models.CharField(verbose_name=u'机房名称', max_length=60)
    address = models.CharField(verbose_name=u'机房地址', max_length=255)
    area = models.CharField(verbose_name=u'机房区域', blank=True, null=True, max_length=60)
    # cabinet = models.ForeignKey('Cabinet', blank=True, null=True, max_length=60)
    create_date = models.DateTimeField(verbose_name=u'创建时间', blank=True, null=True, auto_now_add=True, max_length=32)
    update_date = models.DateTimeField(verbose_name=u'更新时间', blank=True, null=True, auto_now=True, max_length=32)

    class Meta:
        verbose_name = 'IDC机房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


