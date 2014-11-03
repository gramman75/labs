from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
	message = models.CharField(max_length=240)
	user    = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.message