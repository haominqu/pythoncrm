#-*- coding: UTF-8 -*-
from django.http import Http404
from django.http import JsonResponse,request

from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler

from django.contrib.auth.hashers import make_password,check_password
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator

from functools import wraps
from .serializers import *
from .permissions import *
from .models import *
from daily.models import *
import logging
import json
import urllib.request

# @deco({'role': 1})
# @method_decorator(my_login_per)
def my_login_per(func=None):
    @wraps(func)
    def inner(request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        # 登录校验

        print ("hmd",a)
        ret = func(request, *args, **kwargs)
        return ret
        # cookie_k = request.session.get("user01", None)
        # if cookie_k:
        #     # 表示已经登录的用户
        #     ret = func(request, *args, **kwargs)
        #     return ret
        # else:
        #     # 滚去登录
        #     return redirect("/login/")
    return inner
# 登录校验


def deco(arg):
    def _deco(func):
        @wraps(func)
        def __deco(*args,**kwargs):
            print (arg['role'],args)
            token = args.META.get("HTTP_AUTHORIZATION").split(' ')
            user = jwt_decode_handler(token[2])
            # if user['role']==arg['role']:
            #     func(UserLogin(),request)
        return __deco
    return _deco


auth_check = "pythoncrm"

class UserLogin(APIView):

    # permission_classes = (
    #     IsManager,
    # )

    def post(self, request):
        username = request.POST.get("username")
        userpwda = request.POST.get("userpwd")
        # userpwd = make_password(userpwda, auth_check, 'pbkdf2_sha1')
        result = True
        data = {}
        error = ""
        user = ""
        lastlogin=datetime.date.today().strftime("%Y-%m-%d %H:%I:%S")
        # if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        #     ip = request.META['HTTP_X_FORWARDED_FOR']
        # else:
        #     ip = request.META['REMOTE_ADDR']
        # ip =request.META['REMOTE_ADDR']
        # print(ip)
        #
        # apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip="+ip
        # content = urllib.request.urlopen(apiurl).read()
        # data = json.loads(content)['data']
        # code = json.loads(content)['code']
        # print (data)
        # #
        # if code == 0:
        #     print "ip:%s from %s%s%s \n" % (data["ip"].encode('utf-8'), data["country"].encode('utf-8'), data["region"].encode('utf-8'),data["city"].encode('utf-8'))
        # else:
        #     print data.encode('utf-8')








        try:
            user = UserInfo.objects.get(loginname=username)
            userpwd = check_password(userpwda,user.userpwd)
            if userpwd:
                user.lastlogin = lastlogin
                user.save()
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                payload['role'] = user.role
                payload['center_id'] = user.center_id
                data['headimg'] = "http://172.40.70.165:8000/" + str(user.head)
                # data['headimg'] = "http://172.164.1.68:8000/"+str(user.head)
                token = jwt_encode_handler(payload)
                if user.role == 1:
                    data['url'] = "managerindex"
                elif user.role == 2:
                    data['url'] = "harryindex"
                elif user.role == 3:
                    data['url'] = "fengindex"
                elif user.role == 4:
                    data['url'] = "teacherindex"
                elif user.role == 5:
                    data['url'] = "masterindex"
                elif user.role == 7:
                    data['url'] = "eduindex"
                data['token'] = token
            else:
                result = False
                error = "用户名密码错误"
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e

        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self, request):
        # token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        # a = jwt_decode_handler(token[2])
        from daily.cexecl import CreateExcel
        response = CreateExcel(request,41)
        result = True
        data = {}
        error = ""
        return response
        return JsonResponse({"result": result, "data": data, "error": error})



class Manager(APIView):

    permission_classes = (
        ChManager,
    )

    def post(self, request):
        manname = request.POST.get("manname")
        loginname = request.POST.get("email")
        tel = request.POST.get("tel")
        email = request.POST.get("email")
        centerid = request.POST.get("centerid")
        leaderid = request.POST.get("leaderid")
        center = Center.objects.filter(id=centerid)
        leader = UserInfo.objects.filter(id=leaderid)
        userisonly = UserInfo.objects.filter(loginname=loginname)
        userpwd = make_password("python1234", auth_check, 'pbkdf2_sha1')
        num = user_repeat(manname)
        if num != '0':
            manname = manname + num
        if len(userisonly) > 0:
            result = False
            data = ""
            error = "登录名重复"
            return JsonResponse({"result": result, "data": data, "error": error})
        else:
            try:
                UserInfo.objects.create(loginname=loginname,username=manname, userpwd=userpwd, uemail=email, role=1, tel=int(tel), center=center[0], leader=leader[0])
            except ObjectDoesNotExist as e:
                logging.warning(e)
                result = False
                error = e
                print (e, "======")
        result = True
        data = {"manname": manname}
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self, request):
        try:
            userinfo = UserInfo.objects.filter(role=1,delete=False)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        serializer = UserInfoSerializer(userinfo, many=True)
        result = True
        data = serializer.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def delete(self, request):
        managerid = request.data.get("managerid")
        result = True
        data = ""
        error = ""
        print(managerid)
        try:
            userinfo = UserInfo.objects.filter(id=managerid).update(delete=True)
            data = "删除成功"
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result=False
            error=e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})

    def put(self, request):
        managerid = request.data.get("managerid")
        manname = request.data.get("manname")
        tel = request.data.get("tel")
        email = request.data.get("email")
        result = True
        data = ""
        error = ""
        try:
            UserInfo.objects.filter(id=managerid).update(username=manname, uemail=email, tel=int(tel))
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})


# post add center
# get select all center
class Centers(APIView):

    permission_classes = (
        IsCenter,
    )

    def post(self, request):
        cname = request.POST.get("cname")
        ads = request.POST.get("ads")
        leader = request.POST.get("leader")
        tel = request.POST.get("tel")
        result = True
        data = {"msg": "success"}
        error = ""
        try:
            Center.objects.create(cname=cname, ads=ads, leader=leader, tel=tel)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data=""
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self, request):
        center = Center.objects.filter(delete=False)
        serializer = CenterSerializer(center, many=True)
        result = True
        data = serializer.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def delete(self, request):
        centerid = request.data.get("centerid")
        result = True
        data = ""
        error = ""
        try:
            centerinfo = Center.objects.filter(id=centerid).update(delete=True)
            data = "删除成功"
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})

    def put(self, request):
        centerid = request.data.get("centerid")
        cname = request.data.get("cname")
        ads = request.data.get("ads")
        leader = request.data.get("leader")
        tel = request.data.get("tel")
        result = True
        data = ""
        error = ""
        try:
            centerinfo = Center.objects.filter(id=centerid).update(cname=cname, ads=ads, leader=leader, tel=tel)
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
        return JsonResponse({"result": result, "data": data, "error": error})


# this func is about class
class ClassesAPI(APIView):

    permission_classes = (
        IsClasses,
    )

    def post(self, request):
        classno = request.POST.get('classno')
        month = datetime.date.today().strftime("%Y%m")
        result = True
        data = {"msg": "success"}
        error = ""
        try:
            centers = Center.objects.filter(delete=False)
            oldclass = Classes.objects.filter(classno=classno)
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if len(oldclass)>0:
            result = False
            data = ""
            error = "已存在该班级"
        else:
            for center in centers:
                try:
                    print(center)
                    classes = Classes.objects.create(classno=classno, classname=classno+center.cname, center=center)
                    Classday.objects.create(classes=classes, month=0, day=0, monthtruth=month)
                except ObjectDoesNotExist as e:
                    logging.warning(e)
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self, request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        if a['role'] == 2:
            classes = Classes.objects.filter(delete=False)
        elif a['role'] == 7:
            classes = Classes.objects.filter(center_id=a["center_id"],delete=False)
        elif a['role'] == 1:
            classes = Classes.objects.filter(manager_id=a["user_id"],delete=False, active=True)
        elif a['role'] == 5:
            classes = Classes.objects.filter(master_id=a["user_id"], active=True, delete=False)
        serializer = ClassesSerializer(classes, many=True)
        result = True
        data = serializer.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def delete(self, request):
        classid = request.data.get('classid')
        result = True
        data = ""
        error = ""
        print("!!!!!",classid)
        try:
            daily = Classday.objects.filter(classes_id=classid).delete()
            classes = Classes.objects.filter(id=classid).delete()
            data = {'msg':"delete success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})

    def put(self,request):
        classid = request.data.get('classid')
        classno = request.data.get('classno')
        managerid = request.data.get('managerid')
        centerid = request.data.get('centerid')
        result = True
        data = ""
        error = ""
        manager = UserInfo.objects.filter(id=managerid)
        center = Center.objects.filter(id=centerid)
        try:
            classes = Classes.objects.filter(id=classid).update(classno=classno, manager=manager, center=center)
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = e
        return JsonResponse({"result": result, "data": data, "error": error})


class ClassActive(APIView):

    permission_classes = (
        IsClassActive,
    )

    def post(self,request):
        classid = request.POST.get('classid')
        managerid = request.POST.get('managerid')
        masterid = request.POST.get('masterid')
        result = True
        data = ""
        error = ""
        print(managerid,classid,masterid)
        try:
            manager = UserInfo.objects.get(id=managerid)
            master = UserInfo.objects.get(id=masterid)
            classes = Classes.objects.filter(id=classid).update(active=True, manager=manager, master=master)
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = e
        return JsonResponse({"result": result, "data": data, "error": error})

    def delete(self,request):
        classid = request.data.get('classid')
        result = True
        data = ""
        error = ""
        try:
            classes = Classes.objects.filter(id=classid).update(active=False)
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = e
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self,request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        center_id = a['center_id']
        print(center_id)
        try:
            managerinfo =  UserInfo.objects.filter(center_id=center_id,role=1, delete=False)
            masterinfo = UserInfo.objects.filter(center_id=center_id,role=5, delete=False)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            data = ""
            error = e
        serializermn = ManagerSerializer(managerinfo, many=True)
        serializerms = ManagerSerializer(masterinfo, many=True)
        result = True
        datamn = serializermn.data
        datams = serializerms.data
        print(json.dumps(datamn, ensure_ascii=False))
        data = {}
        data['manager']=json.dumps(datamn, ensure_ascii=False)
        data['master']=json.dumps(datams, ensure_ascii=False)
        data = json.dumps(data, ensure_ascii=False)
        error = ""

        return JsonResponse({"result": result, "data": data, "error": error})


class EduAPI(APIView):

    permission_classes = (
        EduPermission,
    )

    def post(self, request):
        centerid = request.POST.get('centerid')
        leaderid = request.POST.get("leaderid")
        eduname = request.POST.get('eduname')
        tel = request.POST.get('tel')
        uemail = request.POST.get('uemail')
        loginname = uemail
        userpwd = make_password("python1234", auth_check, 'pbkdf2_sha1')
        userisonly = UserInfo.objects.filter(loginname=loginname)
        center = Center.objects.filter(id=centerid)
        leader = UserInfo.objects.filter(id=leaderid)
        if len(userisonly) > 0:
            result = False
            data = ""
            error = "登录名重复"
            return JsonResponse({"result": result, "data": data, "error": error})
        else:
            try:
                UserInfo.objects.create(loginname=loginname, username=eduname, userpwd=userpwd, uemail=uemail, role=7, tel=int(tel), center=center[0], leader=leader[0])
            except ObjectDoesNotExist as e:
                logging.warning(e)
                result = False
                error = e
                print (e, "======")
        result = True
        data = {"manname": eduname}
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self, request):
        try:
            userinfo = UserInfo.objects.filter(role=7,delete=False)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        serializer = EduInfoSerializer(userinfo, many=True)
        result = True
        data = serializer.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def delete(self, request):
        eduid = request.data.get("eduid")
        result = True
        data = ""
        error = ""
        try:
            userinfo = UserInfo.objects.filter(id=eduid).update(delete=True)
            data = "删除成功"
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})

    def put(self, request):
        managerid = request.data.get("eduid")
        eduname = request.POST.get('eduname')
        tel = request.data.get("tel")
        email = request.data.get("email")
        result = True
        data = ""
        error = ""
        try:
            UserInfo.objects.filter(id=managerid).update(username=eduname, uemail=email, tel=int(tel))
            data = {"msg": "success"}
        except ObjectDoesNotExist as e:
            logging.warning(e)
            result = False
            error = e
            print (e, "======")
        return JsonResponse({"result": result, "data": data, "error": error})



def user_repeat(username):
    num = ''
    try:
        usern = UserRepeat.objects.filter(username=username)
    except ObjectDoesNotExist as e:
        logging(e)
    if len(usern)>0:
        num = str(usern[0].num+1)
    return num