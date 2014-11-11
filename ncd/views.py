from django.shortcuts import render
from rest_framework import viewsets
from ncd.models import SamSkill, SamEmployee
from ncd.serializers import SamSkillSerializer, SamEmployeeSerializer
from rest_framework.response import Response

# Create your views here.

class SamSkillViewSet(viewsets.ModelViewSet):
	queryset = SamSkill.objects.all()
	serializer_class = SamSkillSerializer

class SamEmployeeViewSet(viewsets.ModelViewSet):
	queryset = SamEmployee.objects.all()
	serializer_class = SamEmployeeSerializer

	def list(self, requeset):
		skill = requeset.QUERY_PARAMS.get('skill')
		print 'skill %s' %skill
		queryset = SamEmployee.objects.filter(skill_code__exact=skill)
		serializer = SamEmployeeSerializer(queryset, many=True)

		return Response(serializer.data)


