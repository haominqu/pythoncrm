from django.shortcuts import render
from rest_framework.views import APIView
from userinfo.models import *
from django.http import JsonResponse,request
from rest_framework_jwt.utils import jwt_decode_handler
from userinfo.serializers import *
from .cexecl import *
from .serializers import *
import datetime
from .models import  *
from django.core.exceptions import ObjectDoesNotExist
import logging
from .permissions import *
from sendemail.views import *
from sendemail.tasks import *

class DailyDetail(APIView):

    def post(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        managerid = a['user_id']
        classes = Classes.objects.filter(manager=managerid)
        # students = StudentInfo.objects.filter(classes = classes[0])
        teacher = UserInfo.objects.filter(role=4)
        manager = UserInfo.objects.filter(id=managerid)
        result = True
        data = {}
        error = ""
        teacherserializer = TeacherInfoSerializer(teacher, many=True)
        teacherdata = teacherserializer.data
        data['teacher'] = teacherdata
        data['center'] = classes[0].center.cname
        # data['classes'] = classes[0].classno
        # studentserializer = StudentInfoSerializer(students, many=True)
        # studentdata = studentserializer.data
        # data['students'] = studentdata
        classesd = ClassesSerializer(classes, many=True)
        data['classes'] = classesd.data
        data['proman'] = manager[0].username
        data['master'] = classes[0].master.username
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self,request):
        pass


class DailyEdit(APIView):

    permission_classes = (
        IsDaily,
    )

    def post(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        managerid = a['user_id']
        dates = datetime.date.today().strftime("%Y%m%d")
        teacherid = request.POST.get('teacher')
        courseday = request.POST.get('courseday')
        center = request.POST.get('center')
        classesid = request.POST.get('classes')
        manager = request.POST.get('manager')
        numofp = int(request.POST.get('numofp'))
        actantnum = int(request.POST.get('actantnum'))
        proman = request.POST.get('proman')
        master = request.POST.get('master')
        pltproblem = request.POST.get('pltproblem')
        solveproblem = request.POST.get('solveproblem')
        detail = request.POST.get('detail')
        stuaction = request.POST.get('stuaction')
        solvedetail = request.POST.get('solvedetail')
        reviewle = request.POST.get('reviewle')
        absence = request.POST.get('absence')
        abshistory = request.POST.get('abshistory')
        amreview = request.POST.get('amreview')
        pmreview = request.POST.get('pmreview')
        pmfinish = request.POST.get('pmfinish')
        stuvip = request.POST.get('stuvip')
        other = request.POST.get('other')
        wom = request.POST.get('wom')
        usera = UserInfo.objects.filter(id=managerid)
        teacher = UserInfo.objects.filter(id=teacherid)
        try:
            classes = Classes.objects.filter(id=classesid,active=True)
            dailys = Daily.objects.create(dates=dates, teacher=teacher[0], courseday=courseday, center=center, classes=classes[0].classno, manager=manager, numofp=numofp, actantnum=actantnum, proman=proman, master=master, pltproblem=pltproblem, solveproblem=solveproblem, detail=detail, stuaction=stuaction, solvedetail=solvedetail, reviewle=reviewle, absence=absence, abshistory=abshistory, amreview=amreview, pmfinish=pmfinish, pmreview=pmreview, stuvip=stuvip, other=other, wom=wom, userid=usera[0])
            send_daily.delay(dailys)
        except ObjectDoesNotExist as e:
            logging(e)
        result = True
        data = {'message': '添加成功'}
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        managerid = a['user_id']
        # date = request.GET.get('date','')
        # try:
        #     if date == '':
        #         daily = Daily.objects.filter(userid_id=managerid)
        #     else:manager
        #         daily = Daily.objects.filter(dates=date,userid_id=managerid)
        # except ObjectDoesNotExist as e:
        #     logging(e)
        if a['role'] == 1 or a['role'] == 7:
            try:
                daily = Daily.objects.filter(userid_id=managerid)
            except ObjectDoesNotExist as e:
                logging(e)
        elif a['role'] == 2:
            try:
                daily = Daily.objects.all()
            except ObjectDoesNotExist as e:
                logging(e)

        result = True
        error = ""
        data = DailyListSerializer(daily, many=True).data
        return JsonResponse({"result": result, "data": data, "error": error})


class DailyShow(APIView):

    def post(self, request):
        dates = request.POST.get("dates")
        pass

    def get(self,request):
        dailyid =request.GET.get('dailyid')
        try:
            daily = Daily.objects.filter(id=dailyid)
        except ObjectDoesNotExist as e:
            logging(e)
        data = DailyDetailSerializer(daily, many=True).data
        result = True
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class HarryNY(APIView):

    permission_classes = (
        IsDaily,
    )

    def get(self, request):

        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        managerid = a['user_id']
        classesid = request.GET.get('classesid')
        data = {}
        try:
            students = StudentInfo.objects.filter(classes_id=classesid, leschool=False)
            classday = Classday.objects.get(classes_id=classesid)
        except ObjectDoesNotExist as e:
            logging(e)
        studs = StudentInfoSerializer(students,many=True)
        data['students'] = studs.data
        data['classesid'] = classesid
        data['classes'] = classday.classes.classno
        print ('@@@@@@@',datetime.date.today().strftime("%Y%m"),type(datetime.date.today().strftime("%Y%m")), classday.monthtruth,type(classday.monthtruth))
        if datetime.date.today().strftime("%Y%m") != str(classday.monthtruth):
            print(datetime.date.today().strftime("%Y%m"))
            try:
                classday.month = classday.month + 1
                classday.day = 1
                classday.monthtruth = datetime.date.today().strftime("%Y%m")
                classday.save()
                data['day'] = classday.day
                data['month'] = classday.month
            except ObjectDoesNotExist as e:
                logging(e)
        else:
            data['day'] = classday.day+1
            data['month'] = classday.month
        result = True
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def post(self,request):
        # token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        # a = jwt_decode_handler(token[2])
        # managerid = a['user_id']
        classesid = request.POST.get('classesid')
        dadata = request.POST.get('data')

        day = request.POST.get('day')
        month = request.POST.get('month')
        studata = json.loads(dadata)

        # indata =

            # if olddata.month == 1:
            #     stud.attendfi = json.loads(stud.attendfi).append(nys)
            # elif olddata.month == 2:
            #
            # elif olddata.month == 3:
            #
            # elif olddata.month == 4:

            # print (stud.id)
        result = True
        error = ""
        data={}

        try:
            olddata = Classday.objects.get(classes_id=classesid)
        except ObjectDoesNotExist as e:
            logging(e)
        if olddata.today == datetime.date.today().strftime("%Y%m%d"):
            result = False
            error = '当天评价已提交，请勿重复提交'
            return JsonResponse({"result": result, "data": data, "error": error})
        else:
            nst = []
            for st in studata:
                nys = {}
                dayo = int(day)
                nys['day' + str(dayo)] = st['ny'] + st['score']
                nst.append(nys)
                try:
                    stud = Attendance.objects.get(stuid_id=st['id'])
                except ObjectDoesNotExist as e:
                    logging(e)
                print("@@@@",olddata.month)
                if olddata.month == 1:
                    c = json.loads(stud.attendfi)
                    c.append(nys)
                    stud.attendfi = json.dumps(c)
                elif olddata.month == 2:
                    c = json.loads(stud.attendse)
                    c.append(nys)
                    stud.attendse = json.dumps(c)
                elif olddata.month == 3:
                    c = json.loads(stud.attendth)
                    c.append(nys)
                    stud.attendth = json.dumps(c)
                elif olddata.month == 4:
                    c = json.loads(stud.attendfo)
                    c.append(nys)
                    stud.attendfo = json.dumps(c)
                try:
                    stud.save()
                except ObjectDoesNotExist as e:
                    logging(e)
            #获取前端数据
            olddata.day = olddata.day+1
            olddata.today = datetime.date.today().strftime("%Y%m%d")
            try:
                olddata.save()
            except ObjectDoesNotExist as e:
                logging(e)
            return JsonResponse({"result": result, "data": data, "error": error})
        return JsonResponse({"result": result, "data": data, "error": error})


class Leader(APIView):


    def get(self,request):
        trole = request.GET.get('add')
        if trole == '1':
            leader = UserInfo.objects.filter(role=7)
        elif trole == '2':
            leader = UserInfo.objects.filter(role=3)
        elif trole == '3':
            leader = UserInfo.objects.filter(role=3)
        elif trole == '4':
            leader = UserInfo.objects.filter(role=3)
        elif trole == '5':
            leader = UserInfo.objects.filter(role=3)
        elif trole == '7':
            leader = UserInfo.objects.filter(role=2)
        serializer = LeaderInfoSerializer(leader, many=True)
        result = True
        data = serializer.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class SendEmail(APIView):

    def get(self,request):
        response = CreateExcel(request)
        return response
        # try:
        #     daily = Daily.objects.filter(id=11)
        # except ObjectDoesNotExist as e:
        #     logging(e)
        # print(daily[0])
        # response = send_email(request, daily[0], 'quhm@tedu.cn')
        # return response

