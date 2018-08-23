from django.shortcuts import render
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives,send_mail
from django.conf import settings


# 发送邮件
def send_email(request,daily,touser):
    num=1
    subject = '当日日报'
    form_email = settings.EMAIL_FROM
    to =touser
    text_content = 'This is an important message'
    html_content = '<table style="width:100%;text-align:center;" border="1px" cellspacing="0"><tr><th colspan="6" >项目经理工作日报</th></tr><tr><td style="width:10%;background-color:#abb2b4">日期</td><td style="width:15%">'+daily.dates+'</td><td style="width:8%;background-color:#abb2b4">讲师</td><td style="width:12%">'+daily.teacher.username+'</td><td style="width:20%;background-color:#abb2b4">课程阶段/天数</td><td style="width:36%">'+daily.courseday+'</td></tr><tr><td style="background-color:#abb2b4">中心名称</td><td>'+daily.center+'</td><td style="background-color:#abb2b4">班级</td><td>'+daily.classes+'</td><td style="background-color:#abb2b4">教学经理</td><td>'+daily.manager+'</td></tr><tr><td style="background-color:#abb2b4">班级人数/出勤</td><td>'+str(daily.numofp)+'/'+str(daily.actantnum)+'</td><td style="background-color:#abb2b4">项目经理</td><td>'+daily.proman+'</td><td style="background-color:#abb2b4">班主任</td><td>'+daily.master+'</td></tr><tr><td colspan="6" style="background-color:#8bd7ee;text-align:center">日常工作</td></tr><tr><td rowspan="2" style="background-color:#fff2cc">设备环境远程平台运行情况</td><td colspan="3" style="background-color:#fff2cc">远程平台出现的问题</td><td colspan="2" style="background-color:#fff2cc">处理结果</td></tr><tr><td colspan="3">'+daily.pltproblem+'</td><td colspan="2">'+daily.solveproblem+'</td></tr><tr><td rowspan="2" style="background-color:#fff2cc">今日教学内容</td><td colspan="3" style="background-color:#fff2cc">今日教学内容</td><td style="background-color:#fff2cc">学生掌握情况</td><td style="background-color:#fff2cc">项目经理解决措施/建议/求助</td></tr><tr><td colspan="3">'+daily.detail+'</td><td>'+daily.stuaction+'</td><td>'+daily.solvedetail+'</td></tr><tr><td rowspan="5" style="background-color:#fff2cc">早晚自习情况</td><td>早晚自习</td><td>早/晚：</td><td>'+daily.reviewle+'</td><td style="background-color:#fff2cc">当日缺勤</td><td>'+daily.absence+'</td></tr><tr><td style="background-color:#fff2cc">缺勤历史</td><td colspan="4">'+daily.absence+'</td></tr><tr><td style="background-color:#fff2cc">早自习安排</td><td colspan="4">'+daily.amreview+'</td></tr><tr><td style="background-color:#fff2cc">晚自习内容</td><td colspan="4">'+daily.pmreview+'</td></tr><tr><td style="background-color:#fff2cc">晚自习完成情况</td><td colspan="4">'+daily.pmfinish+'</td></tr><tr><td rowspan="4" style="background-color:#fff2cc">今日关注学员</td><td style="background-color:#fff2cc">姓名</td><td colspan="4" style="background-color:#fff2cc">问题/情况说明	解决方案/建议</td></tr><tr><td style="height:24px"></td><td colspan="4"></td></tr><tr><td style="height:24px"></td><td colspan="4"></td></tr><tr><td style="height:24px"></td><td colspan="4"></td></tr><tr><td style="background-color:#fff2cc">其他反馈事项</td><td colspan="5">关于讲师，授课内容，授课知识点的问题</td></tr><tr><td rowspan="2" style="background-color:#fff2cc">口碑/与回访</td><td style="background-color:#fff2cc">姓名</td><td colspan="4" style="background-color:#fff2cc">情况</td></tr><tr><td style="height:24px"></td><td colspan="4"></td></tr></table>'
    msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    # msg.attach_file('./excel/abc.xls')
    msg.send()
    return HttpResponse("success")


def send_email_file(request,filenames,msg):
    for filename in filenames:
        msg.attach_file(filename)
    return msg