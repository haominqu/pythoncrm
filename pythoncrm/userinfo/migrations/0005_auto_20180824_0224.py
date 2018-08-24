# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_userinfo_lastlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='area',
            field=models.CharField(max_length=200, verbose_name='区', default='86'),
        ),
        migrations.AddField(
            model_name='center',
            name='city',
            field=models.CharField(max_length=200, verbose_name='市', default='86'),
        ),
        migrations.AddField(
            model_name='center',
            name='province',
            field=models.CharField(max_length=200, verbose_name='省', default='86'),
        ),
        migrations.AddField(
            model_name='center',
            name='street',
            field=models.CharField(max_length=200, verbose_name='街道', default='86'),
        ),
    ]
