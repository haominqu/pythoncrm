# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20180802_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='lastlogin',
            field=models.CharField(default='a', max_length=100, verbose_name='最后登陆时间'),
            preserve_default=False,
        ),
    ]
