# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from userinfo.models import *
# Create your models here
import datetime

class Daily(models.Model):
    dates = models.CharField("日期", max_length=40, default=datetime.date.today().strftime("%Y%m%d"))
    teacher = models.ForeignKey(UserInfo, related_name='teacher')
    courseday = models.CharField('课程阶段', max_length=100, null=False)
    center = models.CharField('中心名称', max_length=50, null=False)
    classes = models.CharField('班级', max_length=50, null=False)
    manager = models.CharField('教学经理', max_length=50, null=False)
    numofp = models.IntegerField('应到人数', null=False)
    actantnum = models.IntegerField('实到人数', null=False)
    proman = models.CharField('项目经理', max_length=50, null=False)
    master = models.CharField('班主任', max_length=50, null=False)
    pltproblem = models.CharField('远程平台问题', max_length=200)
    solveproblem = models.CharField('处理结果', max_length=200)
    detail = models.CharField('教学内容', max_length=200, null=False)
    stuaction = models.CharField('学生掌握情况', max_length=100, null=False)
    solvedetail = models.CharField('解决措施', max_length=200, null=False)
    reviewle = models.CharField('早晚仔细', max_length=50, null=False)
    absence = models.CharField('当日缺勤', max_length=100, null=False)
    abshistory = models.CharField('缺勤历史', max_length=100, null=False)
    amreview = models.CharField('早自习安排', max_length=200, null=False)
    pmreview = models.CharField('晚自习内容', max_length=200, null=False)
    pmfinish = models.CharField('晚自习完成情况', max_length=200, null=False)
    stuvip = models.CharField('今日关注学员', max_length=300)
    other = models.CharField('其他反馈事项', max_length=200)
    wom = models.CharField('口碑与回访', max_length=50)
    userid = models.ForeignKey(UserInfo, related_name='userid')

    def __str__(self):
        return self.proman+"_"+self.dates


class Attendance(models.Model):
    stuid = models.ForeignKey(StudentInfo, verbose_name='stuid',on_delete=models.CASCADE)
    userid = models.ForeignKey(UserInfo, verbose_name='userid')
    classid = models.ForeignKey(Classes, verbose_name='classid')
    attendfi = models.CharField('一月工作日出勤', max_length=1000, null=False, default='[]')
    attendse = models.CharField('二月工作日出勤', max_length=1000, null=False, default='[]')
    attendth = models.CharField('三月工作日出勤', max_length=1000, null=False, default='[]')
    attendfo = models.CharField('四月工作日出勤', max_length=1000, null=False, default='[]')
    score = models.IntegerField('工作日得分',default=0)
    wattend = models.CharField('周六出勤', max_length=50, null=False)
    wscore = models.IntegerField('周六得分',default=0)
    fatfito = models.FloatField('一月出勤情况', default=0.00)
    fdailyp = models.FloatField('一月每日一练', default=0.00)
    satfito = models.FloatField('二月出勤情况', default=0.00)
    sdailyp = models.FloatField('二月每日一练', default=0.00)
    tatfito = models.FloatField('三月出勤情况', default=0.00)
    tdailyp = models.FloatField('三月每日一练', default=0.00)
    foatfito = models.FloatField('四月出勤情况', default=0.00)
    fodailyp = models.FloatField('四月每日一练', default=0.00)
    fvatfito = models.FloatField('五月出勤情况', default=0.00)
    fvdailyp = models.FloatField('五月每日一练', default=0.00)
    projfi = models.CharField('项目完成', max_length=50, null=False, default='[]')
    mothex = models.CharField('每月一考', max_length=50, null=False, default='[]')
    ability = models.CharField('能力考核', max_length=50, null=False, default='[]')
    tolat = models.FloatField('总出勤情况', default=0.00)
    tolda = models.FloatField('总基础知识', default=0.00)
    tolpro = models.FloatField('总项目评分', default=0.00)
    tolmoth = models.FloatField('总月考成绩', default=0.00)
    tolabi = models.FloatField('总能力考核', default=0.00)
    tolshow = models.IntegerField('技术表达', default=0)
    toltech = models.IntegerField('技能评价', default=0)
    tolcom = models.IntegerField('沟通能力', default=0)
    tolchan = models.IntegerField('应变能力', default=0)
    totle = models.FloatField('总综合得分', default=0.00)
    backg = models.IntegerField('背景评价',default=0)
    alltotle = models.FloatField('总综合评定', default=0.00)

    def __str__(self):
        return self.stuid.sname


class Classday(models.Model):
    classes = models.ForeignKey(Classes, verbose_name='classes', on_delete=models.CASCADE)
    month = models.IntegerField('月数', default=1)
    day = models.IntegerField('天数', default=1)
    monthtruth = models.IntegerField('月份')
    today = models.CharField('当天日期', max_length=40, default=datetime.date.today().strftime("%Y%m%d"))

    def __str__(self):
        return self.classes.classname