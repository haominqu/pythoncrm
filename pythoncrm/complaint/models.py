# -*- coding: utf-8 -*-
from django.db import models
from userinfo.models import StudentInfo,UserInfo
# Create your models here.


COCLASSIFY = (
        (1, '建议'),
        (2, '赞美'),
        (3, '疑问'),
        (4, '投诉'),
    )

SCHEDULE = (
        (1, '已提交'),
        (2, '处理中'),
        (3, '反馈中'),
        (4, '已完成'),
        (5, '已取消'),
    )


class Complaint(models.Model):
    stuid = models.ForeignKey(StudentInfo, verbose_name='学生')
    classes = models.CharField('班级', max_length=100, null=False)
    teacher = models.ForeignKey( UserInfo, verbose_name='讲师')
    coclassify = models.IntegerField('投诉分类', choices=COCLASSIFY, default=1)
    detail = models.TextField('投诉内容')
    tel = models.CharField('电话', max_length=50, null=False)
    cotime = models.DateTimeField('投诉时间', auto_now_add=True)
    solve = models.BooleanField('是否解决', default=False)
    solvede = models.TextField('投诉解决方案',null=True)
    schedule = models.IntegerField('投诉进度', choices=SCHEDULE, default=1)

    def get_coclassify(self):
        if self.coclassify == 1:
            return u'建议'
        elif self.coclassify == 2:
            return u'赞美'
        elif self.coclassify == 3:
            return u'疑问'
        elif self.coclassify == 4:
            return u'投诉'

    def get_schedule(self):
        if self.schedule == 1:
            return u'已提交'
        elif self.schedule == 2:
            return u'处理中'
        elif self.schedule == 3:
            return u'反馈中'
        elif self.schedule == 4:
            return u'已完成'
        elif self.schedule == 5:
            return u'已取消'