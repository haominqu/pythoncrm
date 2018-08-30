# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0005_auto_20180824_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='direction',
            field=models.IntegerField(verbose_name='就业方向', default=1, choices=[(0, 'web'), (1, '爬虫'), (2, '数据分析'), (3, '人工智能'), (4, '量化交易'), (5, '嵌入式'), (6, '前端')]),
        ),
    ]
