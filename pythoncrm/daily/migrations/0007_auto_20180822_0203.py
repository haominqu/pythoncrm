# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0006_auto_20180802_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classday',
            name='today',
            field=models.CharField(default='20180822', max_length=40, verbose_name='当天日期'),
        ),
        migrations.AlterField(
            model_name='daily',
            name='dates',
            field=models.CharField(default='20180822', max_length=40, verbose_name='日期'),
        ),
    ]
