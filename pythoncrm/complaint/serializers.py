# -*- coding:utf-8 -*-

from rest_framework import serializers
from userinfo.serializers import *
from daily.serializers import *
from .models import *
from userinfo.models import *
import json

class ComplaintStuSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentInfo
		fields = ('sname')


class ComplaintSerializer(serializers.ModelSerializer):


	stuid = serializers.SerializerMethodField('stuid_field')
	def stuid_field(self, obj):
		return obj.stuid.sname

	teacher = serializers.SerializerMethodField('teacher_field')
	def teacher_field(self, obj):
		return obj.teacher.username

	codate = serializers.SerializerMethodField('codate_field')
	def codate_field(self, obj):
		time = obj.cotime.strftime("%Y-%m-%d")
		return time

	cotime = serializers.SerializerMethodField('cotime_field')
	def cotime_field(self, obj):
		time = obj.cotime.strftime("%H:%I:%S")
		return time

	coclassifyd = serializers.SerializerMethodField('coclassify_field')
	def coclassify_field(self, obj):
		return obj.get_coclassify()

	scheduled = serializers.SerializerMethodField('schedule_field')
	def schedule_field(self, obj):
		return obj.get_schedule()

	class Meta:
		model = Complaint
		fields = ('id','stuid','classes','teacher','coclassify','coclassifyd','detail','tel','codate','cotime','schedule','scheduled','solvede')
