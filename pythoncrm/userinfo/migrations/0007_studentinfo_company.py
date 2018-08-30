# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0006_studentinfo_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='company',
            field=models.CharField(max_length=50, null=True, verbose_name='就业公司'),
        ),
    ]
