#-*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.http import StreamingHttpResponse
import xlwt
from userinfo.models import *
from .models import *
# import StringIO
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
import logging
import json

def CreateExcel(request,classid):
    try:
        classtruth = Classes.objects.filter(id=classid)
    except ObjectDoesNotExist as e:
        logging(e)
    wb = xlwt.Workbook(encoding='utf-8')
    # xlwt.add_palette_colour("custom_colour", 0x23)
    style_heading = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour dark_red_ega;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )
    style_heading_pup = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour purple_ega;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_heading_blue = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour ocean_blue;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_heading_lav = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour lavender;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_heading_green = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour dark_green_ega;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_heading_orange = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour orange;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_heading_red = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour red;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_headingg = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index white,
                    bold on,
                    height 0xA0;
                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour gray_ega;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                                )

    style_title = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour coral;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_titleb = xlwt.easyxf("""
            font:
                name Arial,
                colour_index black,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour coral;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_body = xlwt.easyxf("""
            font:
                name Arial,
                colour_index black,
                bold on,
                height 0xA0;
                
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour white;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """
                               )

    style_nygreen = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index green,
                    bold on,
                    height 0xA0;

                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour light_green;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                             )

    style_nyred = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index red,
                    bold on,
                    height 0xA0;

                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour coral;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                             )

    style_scgreen = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index green,
                    bold on,
                    height 0xA0;

                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour white;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                             )

    style_scred = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index red,
                    bold on,
                    height 0xA0;

                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour white;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                             )

    wso = wb.add_sheet(u'学院情况')
    wso.write_merge(0, 0, 0, 9, u'基本信息',style_heading)
    wso.write(1, 0, u'系列班', style_title)
    wso.write_merge(1, 1, 1, 9, classtruth[0].classno, style_title)
    wso.write(2, 0, u'学员姓名', style_title)
    wso.write(2, 1, u'性别', style_title)
    wso.write(2, 2, u'年龄', style_title)
    wso.write(2, 3, u'学历', style_title)
    wso.write(2, 4, u'毕业院校', style_title)
    wso.write(2, 5, u'专业', style_title)
    wso.write(2, 6, u'工作经验', style_title)
    wso.write(2, 7, u'手机', style_title)
    wso.write(2, 8, u'QQ', style_title)
    wso.write(2, 9, u'备注', style_title)
    try:
        studs = Attendance.objects.filter(classid=4)
    except ObjectDoesNotExist as e:
        logging(e)
    for inx, stud in enumerate(studs):
        wso.write(int(inx)+3, 0, stud.stuid.sname, style_body)
        wso.write(int(inx)+3, 1, stud.stuid.get_sex_display(), style_body)
        wso.write(int(inx)+3, 2, stud.stuid.age, style_body)
        wso.write(int(inx)+3, 3, stud.stuid.get_edu_display(), style_body)
        wso.write(int(inx)+3, 4, stud.stuid.university, style_body)
        wso.write(int(inx)+3, 5, stud.stuid.major, style_body)
        wso.write(int(inx)+3, 6, stud.stuid.get_workbg_display(), style_body)
        wso.write(int(inx)+3, 7, stud.stuid.mobile, style_body)
        wso.write(int(inx)+3, 8, stud.stuid.QQ, style_body)
        wso.write(int(inx)+3, 9, stud.stuid.remark, style_body)
    try:
        stuny = Attendance.objects.filter(classid_id=4)
    except ObjectDoesNotExist as e:
        logging(e)


    wss = wb.add_sheet(u'工作记录_M01')
    wss.write_merge(0, 0, 0, 1, u'基本信息', style_heading)
    wss.write_merge(0, 0, 2, 55, u'学习记录', style_headingg)
    wss.write_merge(1, 1, 0, 1, u'AID1803', style_title)
    c = 1
    for j in range(2, 46, 2):
        wss.write_merge(1, 1, j, j+1, u'D'+str(c), style_body)
        c = c+1
    wk = 1
    for x in range(46, 55, 2):
        wss.write_merge(1, 1, x, x+1, u'W'+str(wk), style_headingg)
        wk = wk+1
    wss.write(2, 0, u'学员姓名', style_body)
    wss.write(2, 1, u'备注', style_body)
    for i in range(2, 55,2):
        wss.write(2, i, u'考勤', style_body)
        wss.write(2, i+1, u'作业', style_body)
        wss.col(i).width = 1000
        wss.col(i+1).width = 1000
    for inxc, st in enumerate(stuny):
        wss.write(int(inxc) + 3, 0, st.stuid.sname, style_body)
        wss.write(int(inxc) + 3, 1, st.stuid.nyremark, style_body)
        atfis = json.loads(st.attendfi)
        show = 2
        attday = 0
        toatt = len(atfis)
        dailex = 0
        for inx, atf in enumerate(atfis):
            nyshow = atf['day' + str(int(inx) + 1)][0:1]
            scshow = atf['day' + str(int(inx) + 1)][-1:]
            if nyshow == "y":
                wss.write(int(inxc) + 3, show, nyshow, style_nygreen)
                attday = attday + 1
            else:
                wss.write(int(inxc) + 3, show, nyshow, style_nyred)
            show=show+1
            dailex = dailex + int(scshow)
            if scshow == "0":
                wss.write(int(inxc) + 3, show, scshow, style_scred)
            else:
                wss.write(int(inxc) + 3, show, scshow, style_scgreen)
            show = show+1
        if toatt > 0:
            attend = format(float(attday)/int(toatt)*5,'.2f')
            dailyex = format(float(dailex)/int(toatt),'.2f')
        else:
            attend = 0.00
            dailyex = 0.00
        # wss.write(int(inxc) + 3, 56, xlwt.Formula("""(COUNTIF(C4:BD4,"Y")/COUNTIF(C4:BD4,{"*"}))*5"""), style_scgreen)
        wss.write(int(inxc) + 3, 56, attend, style_scgreen)
        wss.write(int(inxc) + 3, 57, dailyex, style_scgreen)
        st.fatfito = attend
        st.fdailyp = dailyex
        st.tolat = attend
        st.tolda = dailyex
        st.save()
    wss.write_merge(0,2,56, 56, u'出勤情况', style_heading_pup)
    wss.write_merge(0,2,57, 57, u'每日一练', style_heading_blue)
    wss.write_merge(0,2,58, 58, u'项目完成', style_heading_lav)
    wss.write_merge(0,2,59, 59, u'每月一考', style_heading_green)
    wss.write_merge(0,2,60, 60, u'能力考核', style_heading_orange)
    wss.write_merge(0,2,61, 61, u'当月评定', style_heading_red)
    wss.col(0).width = 3000
    wss.col(1).width = 5000



    wst = wb.add_sheet(u'工作记录_M02')
    wst.write_merge(0, 0, 0, 1, u'基本信息', style_heading)
    wst.write_merge(0, 0, 2, 55, u'学习记录', style_headingg)
    wst.write_merge(1, 1, 0, 1, u'AID1803', style_title)
    c = 1
    for j in range(2, 46, 2):
        wst.write_merge(1, 1, j, j + 1, u'D' + str(c), style_body)
        c = c + 1
    wk = 1
    for x in range(46, 55, 2):
        wst.write_merge(1, 1, x, x + 1, u'W' + str(wk), style_headingg)
        wk = wk + 1
    wst.write(2, 0, u'学员姓名', style_body)
    wst.write(2, 1, u'备注', style_body)
    for i in range(2, 55, 2):
        wst.write(2, i, u'考勤', style_body)
        wst.write(2, i + 1, u'作业', style_body)
        wst.col(i).width = 1000
        wst.col(i + 1).width = 1000
    for inxc, st in enumerate(stuny):
        wst.write(int(inxc) + 3, 0, st.stuid.sname, style_body)
        wst.write(int(inxc) + 3, 1, st.stuid.nyremark, style_body)
        atses = json.loads(st.attendse)
        show = 2
        attday = 0
        toatt = len(atses)
        dailex = 0
        for inx, ats in enumerate(atses):
            nyshow = ats['day' + str(int(inx) + 1)][0:1]
            scshow = ats['day' + str(int(inx) + 1)][-1:]
            if nyshow == "y":
                wst.write(int(inxc) + 3, show, nyshow, style_nygreen)
                attday = attday + 1
            else:
                wst.write(int(inxc) + 3, show, nyshow, style_nyred)
            show = show + 1
            dailex = dailex + int(scshow)
            if scshow == "0":
                wst.write(int(inxc) + 3, show, scshow, style_scred)
            else:
                wst.write(int(inxc) + 3, show, scshow, style_scgreen)
            show = show + 1
        if toatt > 0:
            attend = format(float(attday) / int(toatt) * 5, '.2f')
            dailyex = format(float(dailex) / int(toatt), '.2f')
        # wss.write(int(inxc) + 3, 56, xlwt.Formula("""(COUNTIF(C4:BD4,"Y")/COUNTIF(C4:BD4,{"*"}))*5"""), style_scgreen)
        else:
            attend = 0.00
            dailyex = 0.00
        wst.write(int(inxc) + 3, 56, attend, style_scgreen)
        wst.write(int(inxc) + 3, 57, dailyex, style_scgreen)
        st.satfito = attend
        st.sdailyp = dailyex

        if attend != "0.00":
            st.tolat = float(st.tolat) + float(attend)
            st.tolda = float(st.tolda) + float(dailyex)
        st.save()
    wst.write_merge(0,2,56, 56, u'出勤情况', style_heading_pup)
    wst.write_merge(0,2,57, 57, u'每日一练', style_heading_blue)
    wst.write_merge(0,2,58, 58, u'项目完成', style_heading_lav)
    wst.write_merge(0,2,59, 59, u'每月一考', style_heading_green)
    wst.write_merge(0,2,60, 60, u'能力考核', style_heading_orange)
    wst.write_merge(0,2,61, 61, u'当月评定', style_heading_red)



    wsf = wb.add_sheet(u'工作记录_M03')
    wsf.write_merge(0, 0, 0, 1, u'基本信息', style_heading)
    wsf.write_merge(0, 0, 2, 55, u'学习记录', style_headingg)
    wsf.write_merge(1, 1, 0, 1, u'AID1803', style_title)
    c = 1
    for j in range(2, 46, 2):
        wsf.write_merge(1, 1, j, j + 1, u'D' + str(c), style_body)
        c = c + 1
    wk = 1
    for x in range(46, 55, 2):
        wsf.write_merge(1, 1, x, x + 1, u'W' + str(wk), style_headingg)
        wk = wk + 1
    wsf.write(2, 0, u'学员姓名', style_body)
    wsf.write(2, 1, u'备注', style_body)
    for i in range(2, 55, 2):
        wsf.write(2, i, u'考勤', style_body)
        wsf.write(2, i + 1, u'作业', style_body)
        wsf.col(i).width = 1000
        wsf.col(i + 1).width = 1000
    for inxc, st in enumerate(stuny):
        wsf.write(int(inxc) + 3, 0, st.stuid.sname, style_body)
        wsf.write(int(inxc) + 3, 1, st.stuid.nyremark, style_body)
        atths = json.loads(st.attendth)
        show = 2
        attday = 0
        toatt = len(atths)
        dailex = 0
        for inx, att in enumerate(atths):
            nyshow = att['day' + str(int(inx) + 1)][0:1]
            scshow = att['day' + str(int(inx) + 1)][-1:]
            if nyshow == "y":
                wsf.write(int(inxc) + 3, show, nyshow, style_nygreen)
                attday = attday + 1
            else:
                wsf.write(int(inxc) + 3, show, nyshow, style_nyred)
            show = show + 1
            dailex = dailex + int(scshow)
            if scshow == "0":
                wsf.write(int(inxc) + 3, show, scshow, style_scred)
            else:
                wsf.write(int(inxc) + 3, show, scshow, style_scgreen)
            show = show + 1
        if toatt>0:
            attend = format(float(attday) / int(toatt) * 5, '.2f')
            dailyex = format(float(dailex) / int(toatt), '.2f')
        # wss.write(int(inxc) + 3, 56, xlwt.Formula("""(COUNTIF(C4:BD4,"Y")/COUNTIF(C4:BD4,{"*"}))*5"""), style_scgreen)
        else:
            attend = 0.00
            dailyex = 0.00
        wsf.write(int(inxc) + 3, 56, attend, style_scgreen)
        wsf.write(int(inxc) + 3, 57, dailyex, style_scgreen)
        st.tatfito = attend
        st.tdailyp = dailyex

        if attend != "0.00":
            st.tolat = float(st.tolat) + float(attend)
            st.tolda = float(st.tolda) + float(dailyex)
        st.save()
    wsf.write_merge(0, 2, 56, 56, u'出勤情况', style_heading_pup)
    wsf.write_merge(0, 2, 57, 57, u'每日一练', style_heading_blue)
    wsf.write_merge(0, 2, 58, 58, u'项目完成', style_heading_lav)
    wsf.write_merge(0, 2, 59, 59, u'每月一考', style_heading_green)
    wsf.write_merge(0, 2, 60, 60, u'能力考核', style_heading_orange)
    wsf.write_merge(0, 2, 61, 61, u'当月评定', style_heading_red)

    wsfv = wb.add_sheet(u'工作记录_M04')
    wsfv.write_merge(0, 0, 0, 1, u'基本信息', style_heading)
    wsfv.write_merge(0, 0, 2, 55, u'学习记录', style_headingg)
    wsfv.write_merge(1, 1, 0, 1, u'AID1803', style_title)
    c = 1
    for j in range(2, 46, 2):
        wsfv.write_merge(1, 1, j, j + 1, u'D' + str(c), style_body)
        c = c + 1
    wk = 1
    for x in range(46, 55, 2):
        wsfv.write_merge(1, 1, x, x + 1, u'W' + str(wk), style_headingg)
        wk = wk + 1
    wsfv.write(2, 0, u'学员姓名', style_body)
    wsfv.write(2, 1, u'备注', style_body)
    for i in range(2, 55, 2):
        wsfv.write(2, i, u'考勤', style_body)
        wsfv.write(2, i + 1, u'作业', style_body)
        wsfv.col(i).width = 1000
        wsfv.col(i + 1).width = 1000
    for inxc, st in enumerate(stuny):
        wsfv.write(int(inxc) + 3, 0, st.stuid.sname, style_body)
        wsfv.write(int(inxc) + 3, 1, st.stuid.nyremark, style_body)
        atfos = json.loads(st.attendfo)
        show = 2
        attday = 0
        toatt = len(atfos)
        dailex = 0
        for inx, att in enumerate(atfos):
            nyshow = att['day' + str(int(inx) + 1)][0:1]
            scshow = att['day' + str(int(inx) + 1)][-1:]
            if nyshow == "y":
                wsfv.write(int(inxc) + 3, show, nyshow, style_nygreen)
                attday = attday + 1
            else:
                wsfv.write(int(inxc) + 3, show, nyshow, style_nyred)
            show = show + 1
            dailex = dailex + int(scshow)
            if scshow == "0":
                wsfv.write(int(inxc) + 3, show, scshow, style_scred)
            else:
                wsfv.write(int(inxc) + 3, show, scshow, style_scgreen)
            show = show + 1
        if toatt > 0:
            attend = format(float(attday) / float(toatt) * 5, '.2f')
            dailyex = format(float(dailex) / float(toatt), '.2f')
        else:
            attend = 0.00
            dailyex = 0.00
        # wss.write(int(inxc) + 3, 56, xlwt.Formula("""(COUNTIF(C4:BD4,"Y")/COUNTIF(C4:BD4,{"*"}))*5"""), style_scgreen)
        wsfv.write(int(inxc) + 3, 56, attend, style_scgreen)
        wsfv.write(int(inxc) + 3, 57, dailyex, style_scgreen)
        st.foatfito = attend
        st.fodailyp = dailyex
        if attend != "0.00":
            st.tolat = float(st.tolat) + float(attend)
            st.tolda = float(st.tolda) + float(dailyex)
        st.save()
    wsfv.write_merge(0, 2, 56, 56, u'出勤情况', style_heading_pup)
    wsfv.write_merge(0, 2, 57, 57, u'每日一练', style_heading_blue)
    wsfv.write_merge(0, 2, 58, 58, u'项目完成', style_heading_lav)
    wsfv.write_merge(0, 2, 59, 59, u'每月一考', style_heading_green)
    wsfv.write_merge(0, 2, 60, 60, u'能力考核', style_heading_orange)
    wsfv.write_merge(0, 2, 61, 61, u'当月评定', style_heading_red)

    wssi = wb.add_sheet(u'工作记录_M05')
    wssi.write_merge(0, 0, 0, 1, u'基本信息', style_heading)
    wssi.write_merge(0, 0, 2, 55, u'学习记录', style_headingg)
    wssi.write_merge(1, 1, 0, 1, u'AID1803', style_title)
    c = 1
    for j in range(2, 46, 2):
        wssi.write_merge(1, 1, j, j + 1, u'D' + str(c), style_body)
        c = c + 1
    wk = 1
    for x in range(46, 55, 2):
        wssi.write_merge(1, 1, x, x + 1, u'W' + str(wk), style_headingg)
        wk = wk + 1
    wssi.write(2, 0, u'学员姓名', style_body)
    wssi.write(2, 1, u'备注', style_body)
    for i in range(2, 55, 2):
        wssi.write(2, i, u'考勤', style_body)
        wssi.write(2, i + 1, u'作业', style_body)
        wssi.col(i).width = 1000
        wssi.col(i + 1).width = 1000
    for inxc, st in enumerate(stuny):
        wssi.write(int(inxc) + 3, 0, st.stuid.sname, style_body)
        wssi.write(int(inxc) + 3, 1, st.stuid.nyremark, style_body)
        atths = json.loads(st.attendth)
        show = 2
        attday = 0
        toatt = len(atfis)
        dailex = 0
        for inx, att in enumerate(atths):
            nyshow = att['day' + str(int(inx) + 1)][0:1]
            scshow = att['day' + str(int(inx) + 1)][-1:]
            if nyshow == "y":
                wssi.write(int(inxc) + 3, show, nyshow, style_nygreen)
            else:
                wssi.write(int(inxc) + 3, show, nyshow, style_nyred)
            show = show + 1
            if scshow == "0":
                wssi.write(int(inxc) + 3, show, scshow, style_scred)
            else:
                wssi.write(int(inxc) + 3, show, scshow, style_scgreen)
            show = show + 1
        if toatt > 0:
            attend = format(float(attday) / float(toatt) * 5, '.2f')
            dailyex = format(float(dailex) / float(toatt), '.2f')
        else:
            attend = 0.00
            dailyex = 0.00
        # wss.write(int(inxc) + 3, 56, xlwt.Formula("""(COUNTIF(C4:BD4,"Y")/COUNTIF(C4:BD4,{"*"}))*5"""), style_scgreen)

        wssi.write(int(inxc) + 3, 56, attend, style_scgreen)
        wssi.write(int(inxc) + 3, 57, dailyex, style_scgreen)
        st.fvatfito = attend
        st.fvdailyp = dailyex
        if attend != "0.00":
            st.tolat = float(st.tolat) + float(attend)
            st.tolda = float(st.tolda) + float(dailyex)
        st.save()
    wssi.write_merge(0, 2, 56, 56, u'出勤情况', style_heading_pup)
    wssi.write_merge(0, 2, 57, 57, u'每日一练', style_heading_blue)
    wssi.write_merge(0, 2, 58, 58, u'项目完成', style_heading_lav)
    wssi.write_merge(0, 2, 59, 59, u'每月一考', style_heading_green)
    wssi.write_merge(0, 2, 60, 60, u'能力考核', style_heading_orange)
    wssi.write_merge(0, 2, 61, 61, u'当月评定', style_heading_red)


    wssv = wb.add_sheet(u'学员综合评定')
    try:
        classs=Classday.objects.filter(classes_id=4)
    except ObjectDoesNotExist as e :
        logging(e)
    print(classs[0].month)
    for inxc, st in enumerate(stuny):
        tolatsh = float(st.tolat)/classs[0].month
        toldash = float(st.tolda)/classs[0].month
        projfi = json.loads(st.projfi)
        mothex = json.loads(st.mothex)
        ability = json.loads(st.ability)
        showday = len(projfi)
        pt = 0.00
        mt = 0.00
        at = 0.00
        for p in projfi:
            pt = pt + p
        ptc = pt/classs[0].month
        for m in mothex:
            mt = mt + m
        mtc = mt / classs[0].month
        for a in ability:
            at = at + a
        atc = at / classs[0].month
        tolshow = st.tolshow
        toltech = st.toltech
        tolcom = st.tolcom
        tolchan = st.tolchan
        totole = round((tolatsh + toldash + ptc + mtc + atc + tolshow + toltech + tolcom + tolchan)/9, 2)
        backg = st.backg
        alltotle = round((backg+totole)/2, 2)
        wssv.write(int(inxc) + 3, 5, tolatsh, style_scgreen)
        wssv.write(int(inxc) + 3, 6, toldash, style_scgreen)
        wssv.write(int(inxc) + 3, 7, ptc, style_scgreen)
        wssv.write(int(inxc) + 3, 8, mtc, style_scgreen)
        wssv.write(int(inxc) + 3, 9, atc, style_scgreen)
        wssv.write(int(inxc) + 3, 10, tolshow, style_scgreen)
        wssv.write(int(inxc) + 3, 11, toltech, style_scgreen)
        wssv.write(int(inxc) + 3, 12, tolcom, style_scgreen)
        wssv.write(int(inxc) + 3, 13, tolchan, style_scgreen)
        wssv.write(int(inxc) + 3, 14, totole, style_scgreen)
        wssv.write(int(inxc) + 3, 15, backg, style_scgreen)
        wssv.write(int(inxc) + 3, 16, alltotle, style_scgreen)
        if showday==1:
            wss.write(int(inxc) + 3, 58, projfi[0], style_scgreen)
            wss.write(int(inxc) + 3, 59, mothex[0], style_scgreen)
            wss.write(int(inxc) + 3, 60, ability[0], style_scgreen)
        elif showday==2:
            wss.write(int(inxc) + 3, 58, projfi[0], style_scgreen)
            wst.write(int(inxc) + 3, 58, projfi[1], style_scgreen)
            wss.write(int(inxc) + 3, 59, mothex[0], style_scgreen)
            wst.write(int(inxc) + 3, 59, mothex[1], style_scgreen)
            wss.write(int(inxc) + 3, 60, ability[0], style_scgreen)
            wst.write(int(inxc) + 3, 60, ability[1], style_scgreen)
        elif showday==3:
            wss.write(int(inxc) + 3, 58, projfi[0], style_scgreen)
            wst.write(int(inxc) + 3, 58, projfi[1], style_scgreen)
            wsf.write(int(inxc) + 3, 58, projfi[2], style_scgreen)
            wss.write(int(inxc) + 3, 59, mothex[0], style_scgreen)
            wst.write(int(inxc) + 3, 59, mothex[1], style_scgreen)
            wsf.write(int(inxc) + 3, 59, mothex[2], style_scgreen)
            wss.write(int(inxc) + 3, 60, ability[0], style_scgreen)
            wst.write(int(inxc) + 3, 60, ability[1], style_scgreen)
            wsf.write(int(inxc) + 3, 60, ability[2], style_scgreen)
        elif showday==4:
            wss.write(int(inxc) + 3, 58, projfi[0], style_scgreen)
            wst.write(int(inxc) + 3, 58, projfi[1], style_scgreen)
            wsf.write(int(inxc) + 3, 58, projfi[2], style_scgreen)
            wsfv.write(int(inxc) + 3, 58, projfi[3], style_scgreen)
            wss.write(int(inxc) + 3, 59, mothex[0], style_scgreen)
            wst.write(int(inxc) + 3, 59, mothex[1], style_scgreen)
            wsf.write(int(inxc) + 3, 59, mothex[2], style_scgreen)
            wsfv.write(int(inxc) + 3, 59, mothex[3], style_scgreen)
            wss.write(int(inxc) + 3, 60, ability[0], style_scgreen)
            wst.write(int(inxc) + 3, 60, ability[1], style_scgreen)
            wsf.write(int(inxc) + 3, 60, ability[2], style_scgreen)
            wsfv.write(int(inxc) + 3, 60, ability[3], style_scgreen)
        elif showday==5:
            wss.write(int(inxc) + 3, 58, projfi[0], style_scgreen)
            wst.write(int(inxc) + 3, 58, projfi[1], style_scgreen)
            wsf.write(int(inxc) + 3, 58, projfi[2], style_scgreen)
            wsfv.write(int(inxc) + 3, 58, projfi[3], style_scgreen)
            wssi.write(int(inxc) + 3, 58, projfi[4], style_scgreen)
            wss.write(int(inxc) + 3, 59, mothex[0], style_scgreen)
            wst.write(int(inxc) + 3, 59, mothex[1], style_scgreen)
            wsf.write(int(inxc) + 3, 59, mothex[2], style_scgreen)
            wsfv.write(int(inxc) + 3, 59, mothex[3], style_scgreen)
            wssi.write(int(inxc) + 3, 59, mothex[4], style_scgreen)
            wss.write(int(inxc) + 3, 60, ability[0], style_scgreen)
            wst.write(int(inxc) + 3, 60, ability[1], style_scgreen)
            wsf.write(int(inxc) + 3, 60, ability[2], style_scgreen)
            wsfv.write(int(inxc) + 3, 60, ability[3], style_scgreen)
            wssi.write(int(inxc) + 3, 60, ability[4], style_scgreen)

    wssv.write_merge(0, 0, 0, 21, u'基本信息', style_heading)
    wssv.write(1, 0, u'系列班', style_titleb)
    wssv.write_merge(1, 1, 1, 21, u'AID1803', style_titleb)
    wssv.write(2, 0, u'学员姓名', style_titleb)
    wssv.write(2, 1, u'性别', style_titleb)
    wssv.write(2, 2, u'年龄', style_titleb)
    wssv.write(2, 3, u'学历', style_titleb)
    wssv.write(2, 4, u'专业', style_titleb)
    wssv.write(2, 5, u'工作经验', style_titleb)
    wssv.write(2, 6, u'出勤情况', style_titleb)
    wssv.write(2, 7, u'基础知识', style_titleb)
    wssv.write(2, 8, u'项目评分', style_titleb)
    wssv.write(2, 9, u'月考成绩', style_titleb)
    wssv.write(2, 10, u'能力考核', style_titleb)
    wssv.write(2, 11, u'技术表达', style_titleb)
    wssv.write(2, 12, u'技能评价', style_titleb)
    wssv.write(2, 13, u'沟通能力', style_titleb)
    wssv.write(2, 14, u'应变能力', style_titleb)
    wssv.write(2, 15, u'综合得分', style_titleb)
    wssv.write(2, 16, u'背景评价', style_titleb)
    wssv.write(2, 17, u'综合评定', style_titleb)
    wssv.write(2, 18, u'期望薪资', style_titleb)
    wssv.write(2, 19, u'就业薪资', style_titleb)
    wssv.write(2, 20, u'就业时间', style_titleb)
    wssv.write(2, 21, u'备注', style_title)


    # wso.col(2).width = 256*20
    # wss.col(2).width = 256*20
    # wst.col(2).width = 256*20
    # wsf.col(2).width = 256*20
    # wsfv.col(2).width = 256*20
    # wssi.col(2).width = 256*20
    # wssv.col(2).width = 256*20
    filename = 'excel/'+ '达内学员学习档案（'+ classtruth[0].center.cname+'-'+classtruth[0].classno+'）-'+classtruth[0].manager.username
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=example.xls'
    wb.save(filename)
    return response




    # def file_iterator(file_name, chunk_size=512):  # 用于形成二进制数据
    #     with open(file_name, 'rb') as f:
    #         while True:
    #             c = f.read(chunk_size)
    #             if c:
    #                 yield c
    #             else:
    #                 break
    # # 设置HttpResponse的类型
    # response = StreamingHttpResponse(file_iterator(settings.BASE_DIR+settings.STATIC_URL +'Newabc.xls'))
    # response['Content-Type'] = 'application/vnd.ms-excel'
    # response['Content-Disposition'] = 'attachment;filename=user.xls'
    # # new一个文件
    # wb = xlwt.Workbook(encoding='utf-8')
    # # new一个sheet
    # sheet = wb.add_sheet(u'人员表单')
    # # 维护一些样式， style_heading, style_body, style_red, style_green
    #
    # style_heading = xlwt.easyxf("""
    #         font:
    #             name Arial,
    #             colour_index white,
    #             bold on,
    #             height 0xA0;
    #         align:
    #             wrap off,
    #             vert center,
    #             horiz center;
    #         pattern:
    #             pattern solid,
    #             fore-colour 0x19;
    #         borders:
    #             left THIN,
    #             right THIN,
    #             top THIN,
    #             bottom THIN;
    #         """
    #                            )
    # style_body = xlwt.easyxf("""
    #         font:
    #             name Arial,
    #             bold off,
    #             height 0XA0;
    #         align:
    #             wrap on,
    #             vert center,
    #             horiz left;
    #         borders:
    #             left THIN,
    #             right THIN,
    #             top THIN,
    #             bottom THIN;
    #         """
    #                      )
    # style_green = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x11;")
    # style_red = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x0A;")
    # fmts = [
    #     'M/D/YY',
    #     'D-MMM-YY',
    #     'D-MMM',
    #     'MMM-YY',
    #     'h:mm AM/PM',
    #     'h:mm:ss AM/PM',
    #     'h:mm',
    #     'h:mm:ss',
    #     'M/D/YY h:mm',
    #     'mm:ss',
    #     '[h]:mm:ss',
    #     'mm:ss.0',
    # ]
    # style_body.num_format_str = fmts[0]
    #
    # # 写标题栏
    # sheet.write(0, 0, '姓名', style_heading)
    # sheet.write(0, 1, '英文名', style_heading)
    # sheet.write(0, 2, '职位', style_heading)
    # sheet.write(0, 3, '公司电话', style_heading)
    # sheet.write(0, 4, '手机', style_heading)
    # sheet.write(0, 5, 'QQ', style_heading)
    # sheet.write(0, 6, 'MSN', style_heading)
    # sheet.write(0, 7, 'Email', style_heading)
    # sheet.write(0, 8, '办公地点', style_heading)
    # sheet.write(0, 9, '部门', style_heading)
    # sheet.write(0, 10, '人员状态', style_heading)
    #
    # # 写数据
    # row = 1
    #
    # sheet.write(row, 0, 'haomibn', style_body)
    # sheet.write(row, 1, 'usa.eName', style_body)
    # sheet.write(row, 2, 'usa.postion', style_body)
    # sheet.write(row, 3, 'usa.cPhone', style_body)
    # sheet.write(row, 4, 'usa.pPhone', style_body)
    # sheet.write(row, 5, 'usa.qq', style_body)
    # sheet.write(row, 6, 'usa.msn', style_body)
    # sheet.write(row, 7, 'usa.email', style_body)
    # sheet.write(row, 8, 'usa.offAreas', style_body)
    # sheet.write(row, 9, 'usa.depart', style_red)
    #
    #
    # # 写出到IO
    # # output = StringIO.StringIO()
    # wb.save(settings.BASE_DIR+settings.STATIC_URL)
    # print (settings.BASE_DIR+settings.STATIC_URL +'Newabc.xls')
    # # # 重新定位到开始
    # # output.seek(0)
    # # response.write(output.getvalue())
    # return response