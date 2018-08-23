# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='coclassify',
            field=models.IntegerField(default=1, choices=[(1, '建议'), (2, '赞美'), (3, '疑问'), (4, '投诉')], verbose_name='投诉分类'),
        ),
    ]
