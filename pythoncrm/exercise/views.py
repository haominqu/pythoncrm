from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from django.http import JsonResponse,request
from django.core.exceptions import ObjectDoesNotExist
import logging
from .serializers import *
# Create your views here.


class Exercise(APIView):

    def post(self,request):
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        sfirst = request.POST.get('sfirst')
        ssecond = request.POST.get('ssecond')
        sthird = request.POST.get('sthird')
        sfourth = request.POST.get('sfourth')
        level = request.POST.get('level')
        difficult = request.POST.get('difficult')
        knowledge = request.POST.get('knowledge')
        result = True
        data = {}
        error = ""
        quesone = Exercise.objects.filter(question=question)
        if len(quesone) > 0:
            result = False
            error = "问题已存在"
            return JsonResponse({"result": result, "data": data, "error": error})
        try:
            knowledge = Knowledge.objects.get(id=knowledge)
            Exercise.objects.create(question=question,answer=answer,sfirst=sfirst,ssecond=ssecond,sthird=sthird,sfourth=sfourth,level=level,difficult=difficult,knowledge=knowledge)
        except ObjectDoesNotExist as e:
            logging.warning(e)
            print (e, "======")
        data = "添加成功"
        return JsonResponse({"result": result, "data": data, "error": error})

    def get(self,request):
        level = request.GET.get('level')
        if level == "":
            execise = Exercise.objects.all()
        else:
            execise = Exercise.objects.filter(level=level)
        #分页
        pass


class Knowledge(APIView):

    def get(self,request):
        try:
            knowledge = Knowledge.objects.all()
        except ObjectDoesNotExist as e:
            logging(e)
        serializer = KnowledgeSerializer(knowledge, many=True)
        data = serializer.data
        result = True
        data = ""
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})

    def post(self,request):
        pass


class CreateStuExe(APIView):

    def get(self):

        pass