from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse,request
import logging
import json
import urllib.request
from userinfo.models import  *
from django.db.models import Count
from rest_framework_jwt.utils import jwt_decode_handler
from .readdata import *
from analysis.readdata import *

# Create your views here.


class IndexAnalysis(APIView):
    def get(self,request):
        result = ""
        data = {}
        error = ""
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        data["username"] = a["username"]
        data["lastlogin"] = a["lastlogin"]
        apiurl = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=TEDU7&sty=FC2DPFD&token=4f1862fc3b5e77c150a2b985b12db0fd&_=1534927196240"
        content = urllib.request.urlopen(apiurl).read()
        data['stock'] = content.decode().split(',')[4]
        stucount = UserInfo.objects.filter(delete=False).count()
        centercounts = UserInfo.objects.values("center__city","center__province").filter(delete=False).annotate(count=Count('center'))
        citys = str(ReadMapJson(centercounts))
        data['stucount'] = stucount
        data['citys'] = citys
        return JsonResponse({"result": result, "data": data, "error": error})