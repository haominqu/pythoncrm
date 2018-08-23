# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='题目')),
                ('answer', models.CharField(max_length=200, verbose_name='答案')),
                ('sfirst', models.CharField(max_length=200, verbose_name='答案1')),
                ('ssecond', models.CharField(max_length=200, verbose_name='答案2')),
                ('sthird', models.CharField(max_length=200, verbose_name='答案3')),
                ('sfourth', models.CharField(max_length=200, verbose_name='答案4')),
                ('level', models.IntegerField(default=1, verbose_name='阶段', choices=[(1, '第一阶段'), (2, '第二阶段'), (3, '第三阶段'), (4, '第四阶段')])),
                ('difficult', models.IntegerField(default=1, verbose_name='难度', choices=[(1, '简单'), (2, '普通'), (3, '中等'), (4, '困难'), (5, '复杂')])),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseBig',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='题目')),
                ('answer', models.TextField(verbose_name='答案')),
                ('level', models.IntegerField(default=1, verbose_name='阶段', choices=[(1, '第一阶段'), (2, '第二阶段'), (3, '第三阶段'), (4, '第四阶段')])),
                ('difficult', models.IntegerField(default=1, verbose_name='难度', choices=[(1, '简单'), (2, '普通'), (3, '中等'), (4, '困难'), (5, '复杂')])),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='知识点')),
                ('level', models.IntegerField(default=1, verbose_name='阶段', choices=[(1, '第一阶段'), (2, '第二阶段'), (3, '第三阶段'), (4, '第四阶段')])),
            ],
        ),
        migrations.CreateModel(
            name='ManExercise',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('exeid', models.CharField(max_length=200, verbose_name='练习题目id')),
                ('exeaw', models.CharField(max_length=200, verbose_name='回答')),
                ('exescore', models.IntegerField(verbose_name='得分')),
                ('exeerror', models.CharField(max_length=200, verbose_name='错题id')),
                ('exetime', models.DateTimeField(auto_now_add=True, verbose_name='考试时间')),
                ('exenum', models.IntegerField(verbose_name='考试次数')),
                ('exebid', models.CharField(max_length=200, verbose_name='练习大题目id')),
                ('exebaw', models.CharField(max_length=200, verbose_name='大回答')),
                ('exebscore', models.IntegerField(verbose_name='大得分')),
                ('manager', models.ForeignKey(to='userinfo.UserInfo', verbose_name='经理id')),
            ],
        ),
        migrations.CreateModel(
            name='StuExercise',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('exeid', models.CharField(max_length=200, verbose_name='练习题目id')),
                ('exeaw', models.CharField(max_length=200, verbose_name='回答')),
                ('exescore', models.IntegerField(verbose_name='得分')),
                ('exeerror', models.CharField(max_length=200, verbose_name='错题id')),
                ('exetime', models.DateTimeField(auto_now_add=True, verbose_name='考试时间')),
                ('exenum', models.IntegerField(verbose_name='考试次数')),
                ('stuid', models.ForeignKey(to='userinfo.StudentInfo', verbose_name='学生id')),
            ],
        ),
        migrations.AddField(
            model_name='exercisebig',
            name='knowledge',
            field=models.ForeignKey(to='exercise.Knowledge'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='knowledge',
            field=models.ForeignKey(to='exercise.Knowledge'),
        ),
    ]
