# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('attendfi', models.CharField(default='[]', max_length=1000, verbose_name='一月工作日出勤')),
                ('attendse', models.CharField(default='[]', max_length=1000, verbose_name='二月工作日出勤')),
                ('attendth', models.CharField(default='[]', max_length=1000, verbose_name='三月工作日出勤')),
                ('attendfo', models.CharField(default='[]', max_length=1000, verbose_name='四月工作日出勤')),
                ('score', models.IntegerField(verbose_name='工作日得分')),
                ('wattend', models.CharField(max_length=50, verbose_name='周六出勤')),
                ('wscore', models.IntegerField(verbose_name='周六得分')),
                ('fatfito', models.FloatField(default=0.0, verbose_name='一月出勤情况')),
                ('fdailyp', models.FloatField(default=0.0, verbose_name='一月每日一练')),
                ('satfito', models.FloatField(default=0.0, verbose_name='二月出勤情况')),
                ('sdailyp', models.FloatField(default=0.0, verbose_name='二月每日一练')),
                ('tatfito', models.FloatField(default=0.0, verbose_name='三月出勤情况')),
                ('tdailyp', models.FloatField(default=0.0, verbose_name='三月每日一练')),
                ('foatfito', models.FloatField(default=0.0, verbose_name='四月出勤情况')),
                ('fodailyp', models.FloatField(default=0.0, verbose_name='四月每日一练')),
                ('fvatfito', models.FloatField(default=0.0, verbose_name='五月出勤情况')),
                ('fvdailyp', models.FloatField(default=0.0, verbose_name='五月每日一练')),
                ('projfi', models.CharField(default='[]', max_length=50, verbose_name='项目完成')),
                ('mothex', models.CharField(default='[]', max_length=50, verbose_name='每月一考')),
                ('ability', models.CharField(default='[]', max_length=50, verbose_name='能力考核')),
                ('tolat', models.FloatField(default=0.0, verbose_name='总出勤情况')),
                ('tolda', models.FloatField(default=0.0, verbose_name='总基础知识')),
                ('tolpro', models.FloatField(default=0.0, verbose_name='总项目评分')),
                ('tolmoth', models.FloatField(default=0.0, verbose_name='总月考成绩')),
                ('tolabi', models.FloatField(default=0.0, verbose_name='总能力考核')),
                ('tolshow', models.IntegerField(default=0, verbose_name='技术表达')),
                ('toltech', models.IntegerField(default=0, verbose_name='技能评价')),
                ('tolcom', models.IntegerField(default=0, verbose_name='沟通能力')),
                ('tolchan', models.IntegerField(default=0, verbose_name='应变能力')),
                ('totle', models.FloatField(default=0.0, verbose_name='总综合得分')),
                ('backg', models.IntegerField(default=0, verbose_name='背景评价')),
                ('alltotle', models.FloatField(default=0.0, verbose_name='总综合评定')),
                ('classid', models.ForeignKey(to='userinfo.Classes', verbose_name='classid')),
                ('stuid', models.ForeignKey(to='userinfo.StudentInfo', verbose_name='stuid')),
                ('userid', models.ForeignKey(to='userinfo.UserInfo', verbose_name='userid')),
            ],
        ),
        migrations.CreateModel(
            name='Classday',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('month', models.IntegerField(default=1, verbose_name='月数')),
                ('day', models.IntegerField(default=1, verbose_name='天数')),
                ('monthtruth', models.IntegerField(verbose_name='月份')),
                ('today', models.CharField(default='20180622', max_length=40, verbose_name='当天日期')),
                ('classes', models.ForeignKey(to='userinfo.Classes', verbose_name='classes')),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dates', models.CharField(default='20180622', max_length=40, verbose_name='日期')),
                ('courseday', models.CharField(max_length=100, verbose_name='课程阶段')),
                ('center', models.CharField(max_length=50, verbose_name='中心名称')),
                ('classes', models.CharField(max_length=50, verbose_name='班级')),
                ('manager', models.CharField(max_length=50, verbose_name='教学经理')),
                ('numofp', models.IntegerField(verbose_name='应到人数')),
                ('actantnum', models.IntegerField(verbose_name='实到人数')),
                ('proman', models.CharField(max_length=50, verbose_name='项目经理')),
                ('master', models.CharField(max_length=50, verbose_name='班主任')),
                ('pltproblem', models.CharField(max_length=200, verbose_name='远程平台问题')),
                ('solveproblem', models.CharField(max_length=200, verbose_name='处理结果')),
                ('detail', models.CharField(max_length=200, verbose_name='教学内容')),
                ('stuaction', models.CharField(max_length=100, verbose_name='学生掌握情况')),
                ('solvedetail', models.CharField(max_length=200, verbose_name='解决措施')),
                ('reviewle', models.CharField(max_length=50, verbose_name='早晚仔细')),
                ('absence', models.CharField(max_length=100, verbose_name='当日缺勤')),
                ('abshistory', models.CharField(max_length=100, verbose_name='缺勤历史')),
                ('amreview', models.CharField(max_length=200, verbose_name='早自习安排')),
                ('pmreview', models.CharField(max_length=200, verbose_name='晚自习内容')),
                ('pmfinish', models.CharField(max_length=200, verbose_name='晚自习完成情况')),
                ('stuvip', models.CharField(max_length=300, verbose_name='今日关注学员')),
                ('other', models.CharField(max_length=200, verbose_name='其他反馈事项')),
                ('wom', models.CharField(max_length=50, verbose_name='口碑与回访')),
                ('teacher', models.ForeignKey(to='userinfo.UserInfo', related_name='teacher')),
                ('userid', models.ForeignKey(to='userinfo.UserInfo', related_name='userid')),
            ],
        ),
    ]
