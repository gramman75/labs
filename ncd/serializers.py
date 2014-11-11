from rest_framework import serializers
from ncd.models import SamSkill, SamEmployee

class SamSkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = SamSkill
		field = ('code','name')


class SamEmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = SamEmployee
		field = ('num','name','birthdate','ssn','sex','telephone','address','postal','joblevel_code','division_code','department_code','skill_code')
