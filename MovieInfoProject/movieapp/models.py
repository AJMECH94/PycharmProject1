from django.db import models
from django.conf import settings

class UserInfo(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    username= models.CharField(max_length=40)
    password=models.CharField(max_length=50)
    MobileNo=models.IntegerField()
# Create your models here.
