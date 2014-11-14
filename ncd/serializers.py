from rest_framework import serializers
from ncd.models import SamSkill, SamEmployee, SamJobLevel, SamDivision, SamDepartment

class SamSkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = SamSkill
		field = ('code','name')

class SamJobLevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SamJobLevel
		field = ('code','name')

class SamDivisionSerializer(serializers.ModelSerializer):
	class Meta:
		model = SamDivision
		field = ('code','name')

class SamDepartmentSerializer(serializers.ModelSerializer):
	# division = serializers.Field(source='division')
	division = SamDivisionSerializer()
	class Meta:
		model = SamDepartment
		field = ('division','code','name')

class SamEmployeeSerializer(serializers.ModelSerializer):
	department_code = SamDepartmentSerializer()
	joblevel_code = SamJobLevelSerializer()
	division_code = SamDivisionSerializer()
	skill_code = SamSkillSerializer()
	class Meta:
		model = SamEmployee
		field = ('num','name','birthdate','ssn','sex','telephone','address','postal','joblevel_code','division_code','department_code','skill_code')
