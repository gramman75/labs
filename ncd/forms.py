# -*- encoding:utf8 -*-
from django import forms
from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin
from ncd.models import SamJobLevel, SamDivision, SamDepartment, SamSkill, SamEmployee

class EmployeeForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3FormMixin, forms.ModelForm):
	scope_prefix = 'employee_data'
	form_name    = 'emp_data'

	class Meta:
		model = SamEmployee
		fields = ['num','name','birthdate','ssn','sex','telephone','address','postal','joblevel_code','division_code','department_code','skill_code']
	
	# scope_prefix = 'subscribe_data' #Form의 개발 Value를 하나씩 받지 않고 전체를 받기 위함.
	# form_name = 'my_form'           #html의 form tag에서 form_name의 값이 됨. 

	# num = forms.CharField(max_length=10)
	# name = forms.CharField(max_length=100)
	# birthdate = forms.DateField()
	# ssn  = forms.CharField(max_length=30)
	# sex = forms.ComboField()
	# telephone = forms.CharField(max_length=100)
	# address = forms.CharField(max_length=200)
	# postal = forms.CharField(max_length=100)
	# joblevel_code = forms.ModelChoiceField(queryset=SamJobLevel.objects.all())
	# division_code = forms.ModelChoiceField(queryset=SamDivision.objects.all())
	# department_code = forms.ModelChoiceField(queryset=SamDepartment.objects.all())
	# skill_code = forms.ModelChoiceField(queryset=SamSkill.objects.all())
