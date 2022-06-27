from django.db import models

class EMPLOYEE(models.Model):
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    admin = models.CharField(max_length=50)
    lockkey = models.IntegerField()
