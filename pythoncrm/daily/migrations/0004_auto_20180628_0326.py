# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0003_auto_20180626_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classday',
            name='today',
            field=models.CharField(max_length=40, verbose_name='当天日期', default='20180628'),
        ),
        migrations.AlterField(
            model_name='daily',
            name='dates',
            field=models.CharField(max_length=40, verbose_name='日期', default='20180628'),
        ),
    ]
