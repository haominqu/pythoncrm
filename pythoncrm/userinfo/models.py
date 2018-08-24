# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from analysis.readdata import *
# Create your models here.


# user_info is the user table,it is include manage,harry,teacher,master,Mr.Feng role.




ROLE = (
        (1, 'manager'),
        (2, 'harry'),
        (3, 'feng'),
        (4, 'teacher'),
        (5, 'master'),
        (6, 'other'),
        (7, 'edu'),
    )

SEX = (
        (1, '男'),
        (2, '女'),
)

EDUCATION = (
        (0, '高中'),
        (1, '统招大专'),
        (2, '统招本科'),
        (3, '自考专科'),
        (4, '自考本科'),
        (5, '硕士'),
        (6, '博士'),
)

WORKBG = (
        (0, '无'),
        (1, '在读'),
        (2, '1年'),
        (3, '2年'),
        (4, '3年'),
        (5, '4年'),
        (6, '5年'),
        (7, '5-7年'),
        (8, '8-10年'),
        (9, '10年以上'),
        (10, '半年'),
)







class Center(models.Model):
    cname = models.CharField('中心名称', max_length=100, null=False)
    ads = models.CharField('中心地址', max_length=200, null=False)
    leader = models.CharField('中心主任', max_length=200, null=False)
    tel = models.CharField('中心电话', max_length=200,null=False)
    province = models.CharField('省', max_length=200,null=False,default="86")
    city = models.CharField('市', max_length=200,null=False,default="86")
    area = models.CharField('区', max_length=200,null=False,default="86")
    street = models.CharField('街道', max_length=200,null=False,default="86")
    delete = models.BooleanField('删除', default=False)

    def get_local(self):
        data = localjson(self.province,self.city,self.area,self.street)
        return data


    def __str__(self):
        return self.cname


class UserInfo(models.Model):
    loginname =  models.CharField('登录名', max_length=100, null=False, unique=True)
    username = models.CharField('用户名', max_length=100, null=False)
    userpwd = models.CharField('密码', max_length=100, null=False)
    role = models.IntegerField('角色', choices=ROLE, default=5)
    tel = models.CharField('电话', max_length=200,  null=False)
    uemail = models.CharField('Email', max_length=50)
    head = models.ImageField(upload_to='static/image/head', default='normal.jpg')
    delete = models.BooleanField('删除', default=False)
    center = models.ForeignKey(Center)
    leader = models.ForeignKey('self', null=True, blank=True, verbose_name='上级')
    lastlogin = models.CharField('最后登陆时间',max_length=100, null=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']


    def __str__(self):
        return self.username




class Classes(models.Model):
    classno = models.CharField('班级号', max_length=100, null=False, default='AID')
    classname = models.CharField('班级名称', max_length=100, null=False,unique=True)
    manager = models.ForeignKey(UserInfo, verbose_name='项目经理', related_name='manager', null = True)
    master = models.ForeignKey(UserInfo, verbose_name='班主任', related_name='master', null = True)
    center = models.ForeignKey(Center, verbose_name='中心')
    delete = models.BooleanField('是否关闭', default=False)
    active = models.BooleanField('是否启用', default=False)

    def __str__(self):
        return self.classname


class StudentInfo(models.Model):
    username = models.CharField('登录名', max_length=100, null=False)
    sname = models.CharField('用户名', max_length=100, null=False)
    spwd = models.CharField('密码', max_length=100, null=False)
    sex = models.IntegerField('性别', choices=SEX, default=1)
    age = models.IntegerField('年龄')
    edu = models.IntegerField('学历', choices=EDUCATION, default=2)
    university = models.CharField('毕业院校', max_length=200,null=True)
    major = models.CharField('专业', max_length=200, null=True)
    workbg = models.IntegerField('工作经验', choices=WORKBG, default=0)
    mobile = models.CharField('手机', max_length=50, null=True)
    QQ = models.CharField('QQ', max_length=30, null=True)
    remark = models.CharField('备注', max_length=100, null=False, default='无')
    nyremark = models.CharField('ny备注', max_length=100, null=False, default='无')
    classes = models.ForeignKey(Classes, verbose_name='班级')
    employ = models.BooleanField("就业", default=False)
    selery = models.IntegerField("薪资", default=0)
    leschool = models.BooleanField('休学', default=False)
    delete = models.BooleanField('删除', default=False)


    def get_sex(self):
        if self.sex == 1:
            return u'男'
        elif self.sex == 2:
            return u'女'

    def get_edu(self):
        if self.edu == 0:
            return u'高中'
        elif self.edu == 1:
            return u'统招大专'
        elif self.edu == 2:
            return u'统招本科'
        elif self.edu == 3:
            return u'自考专科'
        elif self.edu == 4:
            return u'自考本科'
        elif self.edu == 5:
            return u'硕士'
        elif self.edu == 6:
            return u'博士'

    def get_workbg(self):
        if self.workbg == 0:
            return u'无'
        elif self.workbg == 1:
            return u'在读'
        elif self.workbg == 2:
            return u'1年'
        elif self.workbg == 3:
            return u'2年'
        elif self.workbg == 4:
            return u'3年'
        elif self.workbg == 5:
            return u'4年'
        elif self.workbg == 6:
            return u'5年'
        elif self.workbg == 7:
            return u'5-7年'
        elif self.workbg == 8:
            return u'8-10年'
        elif self.workbg == 9:
            return u'10年以上'
        elif self.workbg == 10:
            return u'半年'

    def get_classes(self):
        return self.classes.classno

    def __str__(self):
        return self.sname

class UserRepeat(models.Model):
    username = models.CharField('登录名', max_length=100, null=False)
    num = models.IntegerField('重复次数',default=0)