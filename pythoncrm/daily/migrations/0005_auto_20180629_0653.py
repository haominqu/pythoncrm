# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0004_auto_20180628_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classday',
            name='today',
            field=models.CharField(default='20180629', verbose_name='当天日期', max_length=40),
        ),
        migrations.AlterField(
            model_name='daily',
            name='dates',
            field=models.CharField(default='20180629', verbose_name='日期', max_length=40),
        ),
    ]
