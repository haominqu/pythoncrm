# -*- coding:utf-8 -*-

from rest_framework import serializers
from .models import *
import json
from analysis.readdata import *

class CenterSerializer(serializers.ModelSerializer):


	local = serializers.SerializerMethodField('local_field')

	def local_field(self, obj):
		data = localjson(obj.province, obj.city, obj.area, obj.street)
		return data

	class Meta:
		model = Center
		fields = ('id','cname', 'ads', 'leader', 'tel', 'local')


class LeaderSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserInfo
		fields = ('id','username')


class UserInfoSerializer(serializers.ModelSerializer):

	center = CenterSerializer(many=False, read_only=True)
	leader = LeaderSerializer(many=False, read_only=True)

	class Meta:
		model = UserInfo
		fields = ('id','loginname','username','role','tel','uemail','center','leader','head')


class ManagerSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserInfo
		fields = ('id', 'username')


class MasterSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserInfo
		fields = ('id', 'username')

class ClassesSerializer(serializers.ModelSerializer):


	center = CenterSerializer(many=False, read_only=True)
	manager = ManagerSerializer(many=False, read_only=True)
	master = MasterSerializer(many=False, read_only=True)

	class Meta:
		model = Classes
		fields = ('id', 'classno','classname', 'manager','master', 'center','active')

class EduInfoSerializer(serializers.ModelSerializer):
	center = serializers.SerializerMethodField('center_field')

	def center_field(self, obj):
		return obj.center.cname

	leader = LeaderSerializer(many=False, read_only=True)

	class Meta:
		model = UserInfo
		fields = ('id','loginname','username','role','tel','uemail','center','leader','head')
