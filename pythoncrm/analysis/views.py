from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse,request
import logging
import json
import urllib.request
from userinfo.models import  *
from django.db.models import Count,Sum
from rest_framework_jwt.utils import jwt_decode_handler
from .readdata import *
from analysis.readdata import *
from django.views.decorators.cache import cache_page
import random

# Create your views here.
color = ["#9bd598", "#ffd58f", "#abd5f2", "#ab8df2", "#e14f60","#CC0000", "#CC0066", "#66CCFF", "#3300FF", "#CCFF00", ]



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
        centercounts = UserInfo.objects.values("center__city","center__province").filter(delete=False).annotate(count=Count('center')*10)
        citys =  json.dumps(ReadMapJson(centercounts))
        data['stucount'] = stucount
        data['citys'] = citys
        direction = StudentInfo.objects.values("direction").filter(employ=True).annotate(count=Count('direction'),totle=Sum('selery'))
        dire = []
        dires = []
        direses = []
        coloruse =  color
        average = 0
        atotel = 0
        acount = 0
        # coloruse =  random.sample(color, len(direction))
        for v, di in enumerate(direction):
            print(di["direction"],di['totle'])
            direl = {}
            direlse = {}
            if di["direction"] == 0:
                dire.append("n")
                direl["name"] = "n"
                direlse["name"] = "n"
            elif di["direction"] == 1:
                dire.append("爬虫")
                direl["name"] = "爬虫"
                direlse["name"] = "爬虫"
            elif di["direction"] == 2:
                dire.append("数据分析")
                direl["name"] = "数据分析"
                direlse["name"] = "数据分析"
            elif di["direction"] == 3:
                dire.append("人工智能")
                direl["name"] = "人工智能"
                direlse["name"] = "人工智能"
            elif di["direction"] == 4:
                dire.append("量化交易")
                direl["name"] = "量化交易"
                direlse["name"] = "量化交易"
            elif di["direction"] == 5:
                dire.append("嵌入式")
                direl["name"] = "嵌入式"
                direlse["name"] = "嵌入式"
            elif di["direction"] == 6:
                dire.append("前端")
                direl["name"] = "前端"
                direlse["name"] = "前端"
            elif di["direction"] == 7:
                dire.append("web")
                direl["name"] = "web"
                direlse["name"] = "web"
            atotel = atotel+di['totle']
            acount = acount+di["count"]
            direl["value"] = di["count"]
            # direl["itemStyle"] = "{normal: {color: '"+coloruse[v]+"'}}"
            direl["itemStyle"] = {}
            direl["itemStyle"]["normal"] = {}
            direl["itemStyle"]["normal"]["color"] = coloruse[v]
            direlse["value"] = di['totle']/di["count"]
            direlse["itemStyle"] = {}
            direlse["itemStyle"]["normal"] = {}
            direlse["itemStyle"]["normal"]["color"] = coloruse[v]
            dires.append(direl)
            direses.append(direlse)
        average = atotel/acount
        data['dire'] = json.dumps(dire)
        data['dires'] = json.dumps(dires)
        data['direses'] = json.dumps(direses)
        data['average'] = average


        return JsonResponse({"result": result, "data": data, "error": error})