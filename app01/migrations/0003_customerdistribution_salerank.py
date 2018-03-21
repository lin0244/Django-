# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_customer_recv_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDistribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateField()),
                ('status', models.IntegerField(choices=[(1, '正在跟进'), (2, '已成单'), (3, '3天未跟进'), (4, '15天未成单')], default=1, verbose_name='客户状态')),
                ('memo', models.CharField(max_length=255, verbose_name='更多信息')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealer', to='app01.Customer', verbose_name='客户')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cds', to='app01.UserInfo', verbose_name='客户顾问')),
            ],
        ),
        migrations.CreateModel(
            name='SaleRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('weight', models.IntegerField(verbose_name='权重')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo', verbose_name='用户')),
            ],
        ),
    ]
