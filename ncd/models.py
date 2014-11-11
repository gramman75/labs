from django.db import models

# Create your models here.

class SamSkill(models.Model):
	code = models.CharField(max_length=100)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.code

class SamEmployee(models.Model):
	num = models.CharField(max_length=10)
	name = models.CharField(max_length=100)
	birthdate = models.DateField()
	ssn  = models.CharField(max_length=30)
	sex = models.CharField(max_length=10)
	telephone = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	postal = models.CharField(max_length=100)
	joblevel_code = models.CharField(max_length=100)
	division_code = models.CharField(max_length=100)
	department_code = models.CharField(max_length=100)
	skill_code = models.ForeignKey(SamSkill)

	def __unicode__(self):
		return self.name
