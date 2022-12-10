from django.db import models
from django.contrib.auth.models import User 

class TaskList(models.Model):
	manger=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	task=models.CharField(max_length=255)
	done=models.BooleanField()

	def __str__(self):
		return self.task
		
