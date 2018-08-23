# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_studentinfo_leschool'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='uname',
            new_name='username',
        ),
    ]
