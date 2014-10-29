# -*- encoding:utf8 -*-
from django.db import models
from django.contrib.auth.models import User
YES_NO = (('Y','Yes'),
		  ('N','No'),
		  )

class Boards(models.Model):
	BOARD_TYPE = (
		('A', '일반'),
		('B', '경제'),
		('C', '연예 '),
		)
	type      = models.CharField(choices=BOARD_TYPE, max_length = 10)
	title     = models.CharField(max_length = 240)
	comment   = models.TextField()
	startDate = models.DateTimeField();
	endDate	  = models.DateTimeField(null=True)
	enabled   = models.CharField(choices=YES_NO, default='N', max_length=1)
	timestamp = models.DateTimeField(auto_now_add = True)
	user      = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

class Posts(models.Model):
	board = models.ForeignKey(Boards) 
	title = models.CharField(max_length = 240)
	contents = models.TextField()
	block    = models.CharField(choices=YES_NO, default = 'N', max_length=1)
	group    = models.DecimalField(max_digits=100000 , decimal_places = 10)
	seq      = models.DecimalField(max_digits=100000 , decimal_places = 10)
	level    = models.DecimalField(max_digits=100000 , decimal_places = 10)
	createdBy = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Replies(models.Model):
	post = models.ForeignKey(Posts)
	contents = models.TextField()
	block    = models.CharField(choices=YES_NO, default = 'N', max_length=1)
	group    = models.DecimalField(max_digits=100000 , decimal_places = 10)
	seq      = models.DecimalField(max_digits=100000 , decimal_places = 10)
	level    = models.DecimalField(max_digits=100000 , decimal_places = 10)
	createdBy = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.contents