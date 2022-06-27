from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    Phone = models.CharField(max_length=10)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()


class MovieInfo(models.Model):
    uid = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Genres = models.CharField(max_length=500)

class Mycollection(models.Model):
    user = models.ManyToManyField(User,blank=True)
    id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Genres = models.CharField(max_length=500)

