from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse,request
from rest_framework_jwt.utils import jwt_decode_handler
from userinfo.models import *
from django.core.exceptions import ObjectDoesNotExist
import logging
from .models import *
from .serializers import *
from .permissions import *
from userinfo.models import UserInfo

# the studrent post complait
class ComplaintP(APIView):

    permission_classes = (
        IsStudrent,
    )

    def post(self, request):
        print("aaa")
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        studrentid = a['user_id']
        teacherid = request.POST.get('teacherid')
        coclassify = request.POST.get('coclassify')
        detail = request.POST.get('detail')
        tel = request.POST.get('tel')

        try:
            studrent = StudentInfo.objects.filter(id=studrentid)
            teacher = UserInfo.objects.filter(id=teacherid)

        except ObjectDoesNotExist as e:
            logging(e)
        try:

            order = Complaint.objects.create(stuid=studrent[0], classes=studrent[0].classes.classno, teacher=teacher[0], coclassify=coclassify, detail=detail,tel=tel,solve=False)
        except ObjectDoesNotExist as e:
            logging(e)
        result = True
        data = {"msg":"信息已提交", "orderid": order.id}
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        studrentid = a['user_id']
        orderid = request.GET.get('orderid','')
        complaitdata = ''
        if orderid=='':
            try:
                complaits = Complaint.objects.filter(stuid=studrentid)
                print(len(complaits))
            except ObjectDoesNotExist as e:
                logging(e)
            complaitserializer = ComplaintSerializer(complaits, many=True)
            complaitdata = complaitserializer.data
        else:
            try:
                details = Complaint.objects.filter(stuid=studrentid, id=orderid)
            except ObjectDoesNotExist as e:
                logging(e)
            complaitserializer = ComplaintSerializer(details, many=True)
            complaitdata = complaitserializer.data
        result = True
        data = {"data": complaitdata}
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def delete(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        studrentid = a['user_id']
        orderid = request.data.get('orderid')
        try:
            complaits = Complaint.objects.filter(id=orderid).update(schedule=5, solve=True)
        except ObjectDoesNotExist as e:
            logging(e)
        result = True
        data = {"msg":"取消成功"}
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


# complait list manager or teacher
class ManagerComplaint(APIView):

    def get(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        managerid = a['user_id']
        role = a['role']
        orderid = request.GET.get('orderid','')
        coclassify = request.GET.get('coclassifyid','')
        if orderid == "":
            if coclassify == "":

                if role==2 or role==3:
                    complaits = Complaint.objects.filter(solve=False)
                elif role == 4:
                    complaits = Complaint.objects.filter(solve=False, teacher=managerid)
            else:
                if role==2 or role==3:
                    complaits = Complaint.objects.filter(solve=False,coclassify=coclassify)
                elif role == 4:
                    complaits = Complaint.objects.filter(solve=False, teacher=managerid,coclassify=coclassify)
            # complaits.schedule = 2
            # complaits.save()
        else:
            if role == 2 or role == 3 or role == 4:
                complaits = Complaint.objects.filter(id=orderid)
                complaits[0].schedule = 3
                complaits[0].save()
        complaitserializer = ComplaintSerializer(complaits, many=True)
        complaitdata = complaitserializer.data
        result = True
        data = {"data":complaitdata}
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def delete(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        managerid = a['user_id']
        orderid = request.data.get('orderid')
        solvede = request.data.get('solvede')
        print("!!!!",orderid)
        print("!!!!",solvede)
        data = {"msg": '解决失败'}
        try:
            complait = Complaint.objects.get(id=orderid)
            complait.solvede = solvede
            complait.solve = True
            complait.schedule = 4
            complait.save()
            data = {"msg": '已解决'}
        except ObjectDoesNotExist as e:
            logging(e)
        result = True
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class AllComplaint(APIView):

    permission_classes = (
        OnlyHarry,
    )

    def get(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        managerid = a['user_id']
        complaits = Complaint.objects.filter(solve=True)
        complaitserializer = ComplaintSerializer(complaits, many=True)
        complaitdata = complaitserializer.data
        result = True
        data = {"data": complaitdata}
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class TeacherList(APIView):

    def get(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        studrentid = a['user_id']
        teachers = UserInfo.objects.filter(role=4)
        teacherserializer = TeacherInfoSerializer(teachers, many=True)
        teacherdata = teacherserializer.data
        result = True
        error = ""
        return JsonResponse({"result": result, "data": teacherdata, "error": error})
