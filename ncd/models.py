#-*- encoding:utf8 -*-
from django.db import models

# Create your models here.

class SamSkill(models.Model):
	code = models.CharField(max_length=100)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class SamJobLevel(models.Model):
	code = models.CharField(max_length=100)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class SamDivision(models.Model):
	code = models.CharField(max_length=100)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class SamDepartment(models.Model):
	division = models.ForeignKey(SamDivision)
	code     = models.CharField(max_length=100)
	name     = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class SamEmployee(models.Model):
	SEX = (('M','남자'),
		   ('F','여자'))
	num = models.CharField(max_length=10)
	name = models.CharField(max_length=100)
	birthdate = models.DateField()
	ssn  = models.CharField(max_length=30)
	sex = models.CharField(choices=SEX, max_length=10)
	telephone = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	postal = models.CharField(max_length=100)
	joblevel_code = models.ForeignKey(SamJobLevel) 
	division_code = models.ForeignKey(SamDivision)
	department_code = models.ForeignKey(SamDepartment)
	skill_code = models.ForeignKey(SamSkill)

	def __unicode__(self):
		return self.name

