from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    uid = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Genres = models.CharField(max_length=500)

class Mycollection(models.Model):
    id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Genres = models.CharField(max_length=500)