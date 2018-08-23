# -*- coding:utf-8 -*-

from rest_framework import serializers
from .models import *
import json


class KnowledgeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Knowledge
		fields = ('id','title', 'level')


class ExerciseSerializer(serializers.ModelSerializer):

	knowledge = KnowledgeSerializer(many=False, read_only=True)

	class Meta:
		model = Exercise
		fields = ('id','question', 'answer', 'sfirst', 'ssecond', 'sthird', 'sfourth', 'level', 'difficult', 'knowledge')



class ExerciseBigSerializer(serializers.ModelSerializer):

	knowledge = KnowledgeSerializer(many=False, read_only=True)

	class Meta:
		model = ExerciseBig
		fields = ('id','question', 'answer', 'level', 'difficult', 'knowledge')

