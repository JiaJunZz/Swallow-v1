# Generated by Django 2.0.4 on 2018-04-20 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_managemant', models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='管理IP')),
                ('ip_other1', models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='其他IP地址1')),
                ('ip_other2', models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='其他IP地址2')),
                ('os_type', models.CharField(blank=True, choices=[('windows', 'Windows'), ('centos', 'Centos'), ('redhat', 'Redhat'), ('ubuntu', 'Ubuntu')], max_length=32, null=True, verbose_name='系统类型')),
                ('os_release', models.CharField(blank=True, max_length=32, null=True, verbose_name='操作系统版本')),
                ('cpu_physics_count', models.SmallIntegerField(blank=True, null=True, verbose_name='物理CPU个数')),
                ('cpu_core_count', models.SmallIntegerField(blank=True, null=True, verbose_name='CPU核数')),
                ('cpu_logic_count', models.SmallIntegerField(blank=True, null=True, verbose_name='逻辑CPU个数')),
                ('mem_capacity', models.IntegerField(blank=True, null=True, verbose_name='内存大小(GB)')),
                ('disk_capacity', models.FloatField(blank=True, null=True, verbose_name='磁盘容量(GB)')),
                ('raid_type', models.CharField(blank=True, choices=[('None', '无raid'), ('Raid0', 'Raid0'), ('Raid1', 'Raid1'), ('Raid5', 'Raid5')], default='None', max_length=64, null=True, verbose_name='raid类型')),
                ('mac_address', models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='MAC地址')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='资产编号')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='序列号SN')),
                ('asset_type', models.CharField(choices=[('server', '服务器'), ('virtual', '虚拟机'), ('firewall', '防火墙'), ('router', '路由器'), ('switch', '防火墙'), ('others', '其他')], max_length=32, verbose_name='资产类型')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='设备型号')),
                ('trade_date', models.DateField(blank=True, max_length=32, null=True, verbose_name='购买日期')),
                ('expire_date', models.DateField(blank=True, max_length=32, null=True, verbose_name='过保日期')),
                ('cabinet', models.CharField(blank=True, max_length=64, null=True, verbose_name='机柜')),
                ('cabinet_uid', models.CharField(blank=True, max_length=64, null=True, verbose_name='u位')),
                ('memo', models.TextField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True, max_length=32, null=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, max_length=32, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '主机',
                'verbose_name_plural': '主机',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='机房名称')),
                ('address', models.CharField(max_length=255, verbose_name='机房地址')),
                ('area', models.CharField(blank=True, max_length=60, null=True, verbose_name='机房区域')),
                ('create_date', models.DateTimeField(auto_now_add=True, max_length=32, null=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, max_length=32, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'IDC机房',
                'verbose_name_plural': 'IDC机房',
            },
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='厂商名称')),
                ('tel_num', models.CharField(blank=True, max_length=32, null=True, verbose_name='支持电话')),
                ('create_date', models.DateTimeField(auto_now_add=True, max_length=32, null=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, max_length=32, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '制造商',
                'verbose_name_plural': '制造商',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='厂商名称')),
                ('tel_num', models.CharField(blank=True, max_length=32, null=True, verbose_name='支持电话')),
                ('create_date', models.DateTimeField(auto_now_add=True, max_length=32, null=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, max_length=32, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(max_length=32, on_delete=django.db.models.deletion.CASCADE, to='asset.IDC', verbose_name='IDC机房'),
        ),
        migrations.AddField(
            model_name='host',
            name='manufactory',
            field=models.ForeignKey(blank=True, max_length=32, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Manufactory', verbose_name='制造商'),
        ),
        migrations.AddField(
            model_name='host',
            name='supplier',
            field=models.ForeignKey(blank=True, max_length=32, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Supplier', verbose_name='供应商'),
        ),
    ]
