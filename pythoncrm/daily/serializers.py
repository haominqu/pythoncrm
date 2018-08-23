# -*- coding:utf-8 -*-

from rest_framework import serializers
from userinfo.models import *
from userinfo.serializers import *
from .models import *
import json



class LeaderInfoSerializer(serializers.ModelSerializer):


	class Meta:
		model = UserInfo
		fields = ('id','username')

# class DailySerializer(serializers.ModelSerializer):
#

class TeacherInfoSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserInfo
		fields = ('id','username')

class StudentInfoSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentInfo
		fields = ('id','sname')

class DailyListSerializer(serializers.ModelSerializer):

	# classes = ClassesSerializer(many=False, read_only=True)

	class Meta:
		model = Daily
		fields = ('id','classes','proman','dates')

class DailyDetailSerializer(serializers.ModelSerializer):

	teacher = TeacherInfoSerializer(many=False, read_only=True)

	class Meta:
		model = Daily
		fields = ('id','dates','teacher','courseday','center','classes','manager','numofp' ,'actantnum','proman','master','pltproblem','solveproblem','detail','stuaction','solvedetail','reviewle','absence','abshistory','amreview','pmreview','pmfinish','stuvip','other','wom' )



