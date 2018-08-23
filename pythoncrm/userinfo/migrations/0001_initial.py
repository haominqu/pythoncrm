# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('cname', models.CharField(max_length=100, verbose_name='中心名称')),
                ('ads', models.CharField(max_length=200, verbose_name='中心地址')),
                ('leader', models.CharField(max_length=200, verbose_name='中心主任')),
                ('tel', models.CharField(max_length=200, verbose_name='中心电话')),
                ('delete', models.BooleanField(default=False, verbose_name='删除')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('classno', models.CharField(default='AID', max_length=100, verbose_name='班级号')),
                ('classname', models.CharField(unique=True, max_length=100, verbose_name='班级名称')),
                ('delete', models.BooleanField(default=False, verbose_name='是否关闭')),
                ('active', models.BooleanField(default=False, verbose_name='是否启用')),
                ('center', models.ForeignKey(to='userinfo.Center', verbose_name='中心')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('uname', models.CharField(max_length=100, verbose_name='登录名')),
                ('sname', models.CharField(max_length=100, verbose_name='用户名')),
                ('spwd', models.CharField(max_length=100, verbose_name='密码')),
                ('sex', models.IntegerField(default=1, verbose_name='性别', choices=[(1, '男'), (2, '女')])),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('edu', models.IntegerField(default=2, verbose_name='学历', choices=[(0, '高中'), (1, '统招大专'), (2, '统招本科'), (3, '自考专科'), (4, '自考本科'), (5, '硕士'), (6, '博士')])),
                ('university', models.CharField(null=True, max_length=200, verbose_name='毕业院校')),
                ('major', models.CharField(null=True, max_length=200, verbose_name='专业')),
                ('workbg', models.IntegerField(default=0, verbose_name='工作经验', choices=[(0, '无'), (1, '在读'), (2, '1年'), (3, '2年'), (4, '3年'), (5, '4年'), (6, '5年'), (7, '5-7年'), (8, '8-10年'), (9, '10年以上'), (10, '半年')])),
                ('mobile', models.CharField(null=True, max_length=50, verbose_name='手机')),
                ('QQ', models.CharField(null=True, max_length=30, verbose_name='QQ')),
                ('remark', models.CharField(default='无', max_length=100, verbose_name='备注')),
                ('nyremark', models.CharField(default='无', max_length=100, verbose_name='ny备注')),
                ('employ', models.BooleanField(default=False, verbose_name='就业')),
                ('selery', models.IntegerField(default=0, verbose_name='薪资')),
                ('delete', models.BooleanField(default=False, verbose_name='删除')),
                ('classes', models.ForeignKey(to='userinfo.Classes', verbose_name='班级')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('loginname', models.CharField(unique=True, max_length=100, verbose_name='登录名')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('userpwd', models.CharField(max_length=100, verbose_name='密码')),
                ('role', models.IntegerField(default=5, verbose_name='角色', choices=[(1, 'manager'), (2, 'harry'), (3, 'feng'), (4, 'teacher'), (5, 'master'), (6, 'other'), (7, 'edu')])),
                ('tel', models.CharField(max_length=200, verbose_name='电话')),
                ('uemail', models.CharField(max_length=50, verbose_name='Email')),
                ('head', models.ImageField(default='normal.jpg', upload_to='static/image/head')),
                ('delete', models.BooleanField(default=False, verbose_name='删除')),
                ('center', models.ForeignKey(to='userinfo.Center')),
                ('leader', models.ForeignKey(null=True, blank=True, to='userinfo.UserInfo', verbose_name='上级')),
            ],
        ),
        migrations.CreateModel(
            name='UserRepeat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='登录名')),
                ('num', models.IntegerField(default=0, verbose_name='重复次数')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='manager',
            field=models.ForeignKey(null=True, to='userinfo.UserInfo', verbose_name='项目经理', related_name='manager'),
        ),
        migrations.AddField(
            model_name='classes',
            name='master',
            field=models.ForeignKey(null=True, to='userinfo.UserInfo', verbose_name='班主任', related_name='master'),
        ),
    ]
