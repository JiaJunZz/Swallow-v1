from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Host, Manufactory, Supplier, IDC


# Register your models here.


class HostAdmin(admin.ModelAdmin):
    list_display = (
        'asset_type', 'name', 'ip_managemant', 'idc', 'os_type', 'cpu_physics_count', 'mem_capacity', 'disk_capacity',)
    search_fields = (
        'name', 'ip_managemant', 'ip_other1', 'ip_other2', 'sn', 'cabinet', 'cabinet_uid', 'mac_address')
    list_filter = (
        'asset_type', 'trade_date', 'expire_date', 'manufactory', 'supplier', 'idc', 'supplier',
        'os_release',
        'os_type')


class ManufactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel_num', 'create_date', 'update_date')
    search_fields = ('name', 'tel_num')
    list_filter = ('name', 'tel_num', 'create_date', 'update_date')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel_num', 'create_date', 'update_date')
    search_fields = ('name', 'tel_num')
    list_filter = ('name', 'tel_num', 'create_date', 'update_date')


class IDCAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'area', 'create_date', 'update_date')
    search_fields = ('name', 'address', 'area')
    list_filter = ('name', 'address', 'area', 'create_date', 'update_date')



admin.site.register(Host, HostAdmin)
admin.site.register(Manufactory, ManufactoryAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(IDC, IDCAdmin)
