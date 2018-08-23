# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToEmail',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('daiorny', models.IntegerField(default=1, choices=[(1, 'daily'), (2, 'harryny')])),
                ('touser', models.ForeignKey(to='userinfo.UserInfo', verbose_name='收件人', related_name='recivea')),
                ('user', models.ForeignKey(to='userinfo.UserInfo', verbose_name='项目经理', related_name='managera')),
            ],
        ),
    ]
