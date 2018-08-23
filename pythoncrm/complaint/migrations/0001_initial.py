# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('classes', models.CharField(max_length=100, verbose_name='班级')),
                ('coclassify', models.IntegerField(default=1, verbose_name='投诉分类', choices=[(1, '建议'), (2, '改进'), (3, '投诉'), (4, '疑问')])),
                ('detail', models.TextField(verbose_name='投诉内容')),
                ('tel', models.CharField(max_length=50, verbose_name='电话')),
                ('cotime', models.DateTimeField(auto_now_add=True, verbose_name='投诉时间')),
                ('solve', models.BooleanField(default=False, verbose_name='是否解决')),
                ('solvede', models.TextField(null=True, verbose_name='投诉解决方案')),
                ('schedule', models.IntegerField(default=1, verbose_name='投诉进度', choices=[(1, '已提交'), (2, '处理中'), (3, '反馈中'), (4, '已完成'), (5, '已取消')])),
                ('stuid', models.ForeignKey(to='userinfo.StudentInfo', verbose_name='学生')),
                ('teacher', models.ForeignKey(to='userinfo.UserInfo', verbose_name='讲师')),
            ],
        ),
    ]
