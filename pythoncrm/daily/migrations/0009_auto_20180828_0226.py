# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0008_auto_20180824_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classday',
            name='today',
            field=models.CharField(verbose_name='当天日期', default='20180828', max_length=40),
        ),
        migrations.AlterField(
            model_name='daily',
            name='dates',
            field=models.CharField(verbose_name='日期', default='20180828', max_length=40),
        ),
    ]
