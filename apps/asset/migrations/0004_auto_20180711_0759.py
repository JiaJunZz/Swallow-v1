# Generated by Django 2.0.4 on 2018-07-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20180702_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='mem_capacity',
            field=models.IntegerField(blank=True, null=True, verbose_name='内存大小(MB)'),
        ),
    ]
