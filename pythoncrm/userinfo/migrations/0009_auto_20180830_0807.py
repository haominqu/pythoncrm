# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0008_auto_20180830_0733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='selery',
            new_name='salary',
        ),
    ]
