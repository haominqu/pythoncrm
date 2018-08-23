# -*- coding:utf-8 -*-

from rest_framework import serializers
from userinfo.models import *
from userinfo.serializers import *
from daily.serializers import *
from .models import *
import json





class StudentListSerializer(serializers.ModelSerializer):

	classes = serializers.SerializerMethodField('class_field')
	sex = serializers.SerializerMethodField('sex_field')
	edu = serializers.SerializerMethodField('edu_field')
	workbg = serializers.SerializerMethodField('workbg_field')

	def class_field(self,obj):
		return  obj.get_classes()

	def sex_field(self,obj):
		return obj.get_sex()

	def edu_field(self,obj):
		return obj.get_edu()

	def workbg_field(self,obj):
		return obj.get_workbg()

	class Meta:
		model = StudentInfo
		fields = ('id','username','sname','sex','age','edu','university','major','workbg','mobile','QQ','remark','classes','employ','selery')

