from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User
# Create your models here.


class ModelFormWithFile(models.Model):
	def get_user_folder(instance,filename):
		print("{0}/{1}/{2}".format(instance.user.username,str(instance.interview_no),str(instance.ques_no) +'.wav'))
		return "{0}/{1}/{2}".format(instance.user.username,str(instance.interview_no),str(instance.ques_no) +'.wav')

	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default='0')
	name = models.CharField(max_length=20,blank=True)
	upload = models.FileField(upload_to=get_user_folder,null=True,blank=True)
	interview_no = models.IntegerField(blank=True,null=True)
	ques_no = models.IntegerField(blank=True,null=True)
	filler_word = models.IntegerField(blank=True,null=True)
	transcript = models.TextField(max_length=100,default="")
	score = models.IntegerField(blank=True,null=True)
	word_per_minute = models.IntegerField(blank=True,null=True)

class UserWiseInterviewDetail(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	interview_no = models.IntegerField(default=0)

