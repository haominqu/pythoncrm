# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0009_auto_20180828_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classday',
            name='today',
            field=models.CharField(max_length=40, default='20180830', verbose_name='当天日期'),
        ),
        migrations.AlterField(
            model_name='daily',
            name='dates',
            field=models.CharField(max_length=40, default='20180830', verbose_name='日期'),
        ),
    ]
