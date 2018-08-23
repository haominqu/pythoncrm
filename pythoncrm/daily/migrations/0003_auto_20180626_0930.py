# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0002_auto_20180625_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='score',
            field=models.IntegerField(default=0, verbose_name='工作日得分'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='wscore',
            field=models.IntegerField(default=0, verbose_name='周六得分'),
        ),
        migrations.AlterField(
            model_name='classday',
            name='today',
            field=models.CharField(max_length=40, default='20180626', verbose_name='当天日期'),
        ),
        migrations.AlterField(
            model_name='daily',
            name='dates',
            field=models.CharField(max_length=40, default='20180626', verbose_name='日期'),
        ),
    ]
