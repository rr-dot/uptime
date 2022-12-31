from django.db import models

# Create your models here.

class Url(models.Model):
	url=models.CharField(max_length=2500)
	cur_status=models.IntegerField()
	exception_msg=models.CharField(max_length=3000,default='')

