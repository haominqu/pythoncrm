from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse,request
import logging
import json
import urllib.request
from userinfo.models import  *

# Create your views here.
class IndexAnalysis(APIView):
    def get(self):
        result = ""
        data = {}
        error = ""
        apiurl = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=TEDU7&sty=FC2DPFD&token=4f1862fc3b5e77c150a2b985b12db0fd&_=1534927196240"
        content = urllib.request.urlopen(apiurl).read()
        data['stock'] = content.decode().split(',')[4]
        stucount = UserInfo.objects.filter(delete=False).count()
        data['stucount'] = stucount

        return JsonResponse({"result": result, "data": data, "error": error})