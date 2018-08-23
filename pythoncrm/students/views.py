from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from userinfo.models import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_decode_handler
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_jwt.settings import api_settings
import logging
from django.http import JsonResponse,request
from daily.models import *
from .serializers import *
from django.db.models import F

auth_check = "pythoncrm"


class Student(APIView):

    def post(self, request):
        uname = request.POST.get('mobile')
        sname = request.POST.get('sname')
        classesid = request.POST.get('classid')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        edu = request.POST.get('edu')
        university = request.POST.get('university')
        major = request.POST.get('major')
        workbg = request.POST.get('workbg')
        mobile = request.POST.get('mobile')
        QQ = request.POST.get('QQ')
        remark = request.POST.get('remark')
        spwd = uname + "123456"
        userpwd = make_password(spwd, auth_check, 'pbkdf2_sha1')
        result = True
        data = ""
        error = ""
        try:
            classes = Classes.objects.get(id=classesid)
            studrent = StudentInfo.objects.create(uname=uname, sname=sname, spwd=userpwd, sex=sex, age=age, edu=edu, university=university, major=major, workbg=workbg, mobile=mobile, QQ=QQ, remark=remark,classes=classes)
            attendance = Attendance.objects.create(stuid=studrent, userid=classes.manager, classid=classes)
            data = {"data": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = str(e)
            print (e, "======")

        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self, request):
        classesid = request.GET.get('classid')
        result = True
        error = ""
        try:
           studrent = StudentInfo.objects.filter(classes_id=classesid, leschool=False)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
        serializer = StudentListSerializer(studrent, many=True)
        data = serializer.data

        if len(studrent)>0:
            classname = studrent[0].classes.classname
            return JsonResponse({"result": result, "classname": classname, "data": data, "error": error})
        return JsonResponse({"result": result, "classname": "", "data": data, "error": error})

    def delete(self, request):
        stuid = request.data.get("stuid")
        result = True
        data = ""
        error = ""
        try:
            daily = StudentInfo.objects.filter(id=stuid).delete()
            # dailyat = Attendance.objects.filter(stuid=stuid).delete()
            data = {'msg': "delete success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})

    def put(self, request):
        stuid = request.data.get("id")
        sname = request.data.get("sname")
        mobile = request.data.get("mobile")
        QQ = request.data.get("QQ")
        remark = request.data.get("remark")
        result = True
        data = ""
        error = ""
        try:
            StudentInfo.objects.filter(id=stuid).update(uname=mobile, sname=sname, mobile=mobile, QQ=QQ, remark=remark)
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})


class StudStatus(APIView):

    def post(self, request):
        stuid = request.POST.get("stuid")
        classesid = request.POST.get("classid")
        date = datetime.date.today().strftime("%Y%m%d")
        result = True
        data = ""
        error = ""
        try:
            classes = Classes.objects.get(id=classesid)
            StudentInfo.objects.filter(id=stuid).update(remark="留级时间：" + date, classes=classes)
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self, request):
        stuid = request.GET.get("stuid",'')
        classesid = request.GET.get("classid",'')
        date = datetime.date.today().strftime("%Y%m%d")
        result = True
        data = ""
        error = ""
        if stuid == "":
            students = StudentInfo.objects.filter(leschool=True)
            serializer = StudentListSerializer(students, many=True)
            data = serializer.data
        else:
            remark =  "休学结束时间："+date
            try:
                classes = Classes.objects.get(id=classesid)
                StudentInfo.objects.filter(id=stuid).update(classes=classes, remark=remark, leschool=False)
                data = {"msg": "success"}
            except ObjectDoesNotExist as e:
                logging.warning(e)
                result = False
                error = e
                print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})

    def delete(self, request):
        stuid = request.data.get("stuid")
        date = datetime.date.today().strftime("%Y%m%d")
        result = True
        data = ""
        error = ""
        try:
            StudentInfo.objects.filter(id=stuid).update(remark="休学开始时间："+date, leschool=True)
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})


class StuClass(APIView):

    def get(self, request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        classes = Classes.objects.filter(center_id=a["center_id"], delete=False, active=True)
        if len(classes)>0:
            serializer = ClassesSerializer(classes, many=True)
            data = serializer.data
        else:
            data={}
        result = True
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class StudLogin(APIView):

    def post(self, request):
        stuname = request.POST.get("stuname")
        stupwda = request.POST.get("stupwd")
        print(stuname,stupwda)
        stupwd = make_password(stupwda, auth_check, 'pbkdf2_sha1')
        print(stupwd)
        result = True
        data = {}
        error = ""
        user = ""
        try:
            user = StudentInfo.objects.get(username=stuname, spwd=stupwd, delete=False, leschool=False)

        except ObjectDoesNotExist as e:
            result = False
            logging.warning(e)
        if user:

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            print("###&&&")
            payload['classesid'] = user.classes.id
            payload['role'] = "25"

            token = jwt_encode_handler(payload)
            data['token'] = token
            data['url'] = "studentindex"
        else:
            result = False
            error = "用户名密码错误"
        return JsonResponse({"result": result, "data": data, "error": error})


class StudentAnalysis(APIView):

    def post(self):
        stuname = request.POST.get("stuname")
