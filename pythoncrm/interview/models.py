# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class ChaExecise(models.Model):
    question = models.CharField('题目', max_length=200)
    sfirst = models.CharField('答案1', max_length=200)
    ssecond = models.CharField('答案2', max_length=200)
    sthird = models.CharField('答案3', max_length=200)
    sfourth = models.CharField('答案4', max_length=200)

    def __str__(self):
        return self.question

class InterviewCha(models.Model):
    red = models.IntegerField('红色')
    green = models.IntegerField('绿色')
    blue = models.IntegerField('蓝色')
    yellow = models.IntegerField('黄色')
    viewname = models.CharField('面试人姓名', max_length=200)

    def __str__(self):
        return self.viewname


class InterviewExe(models.Model):
    exeid = models.CharField('题目id', max_length=200)
    exeaw = models.CharField('回答', max_length=200)
    exescore = models.IntegerField('得分')
    exetime = models.IntegerField('时间')
    interid = models.ForeignKey(InterviewCha, verbose_name='面试人')
