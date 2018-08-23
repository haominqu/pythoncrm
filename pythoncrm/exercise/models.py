# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from userinfo.models import StudentInfo, UserInfo
# Create your models here.

DIFFICULT = (
        (1, '简单'),
        (2, '普通'),
        (3, '中等'),
        (4, '困难'),
        (5, '复杂'),
    )

LEVEL = (
        (1, '第一阶段'),
        (2, '第二阶段'),
        (3, '第三阶段'),
        (4, '第四阶段'),
    )


class Knowledge(models.Model):
    title = models.CharField('知识点', max_length=200)
    level = models.IntegerField('阶段', choices=LEVEL, default=1)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    question = models.CharField('题目', max_length=200)
    answer = models.CharField('答案', max_length=200)
    sfirst = models.CharField('答案1', max_length=200)
    ssecond = models.CharField('答案2', max_length=200)
    sthird = models.CharField('答案3', max_length=200)
    sfourth = models.CharField('答案4', max_length=200)
    level = models.IntegerField('阶段', choices=LEVEL, default=1)
    difficult = models.IntegerField('难度', choices=DIFFICULT, default=1)
    knowledge = models.ForeignKey(Knowledge)

    def __str__(self):
        return self.question


class ExerciseBig(models.Model):
    question = models.CharField('题目', max_length=200)
    answer = models.TextField('答案')
    level = models.IntegerField('阶段', choices=LEVEL, default=1)
    difficult = models.IntegerField('难度', choices=DIFFICULT, default=1)
    knowledge = models.ForeignKey(Knowledge)

    def __str__(self):
        return self.question


class StuExercise(models.Model):
    exeid = models.CharField('练习题目id', max_length=200)
    exeaw = models.CharField('回答', max_length=200)
    exescore = models.IntegerField('得分')
    exeerror = models.CharField('错题id', max_length=200)
    stuid = models.ForeignKey(StudentInfo, verbose_name='学生id')
    exetime = models.DateTimeField(auto_now_add=True, verbose_name='考试时间')
    exenum = models.IntegerField('考试次数')

    def __str__(self):
        return self.stuid


class ManExercise(models.Model):
    exeid = models.CharField('练习题目id', max_length=200)
    exeaw = models.CharField('回答', max_length=200)
    exescore = models.IntegerField('得分')
    exeerror = models.CharField('错题id', max_length=200)
    manager = models.ForeignKey(UserInfo, verbose_name='经理id')
    exetime = models.DateTimeField(auto_now_add=True, verbose_name='考试时间')
    exenum = models.IntegerField('考试次数')
    exebid = models.CharField('练习大题目id', max_length=200)
    exebaw = models.CharField('大回答', max_length=200)
    exebscore = models.IntegerField('大得分')

    def __str__(self):
        return self.manager