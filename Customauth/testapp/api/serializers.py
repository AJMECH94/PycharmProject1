from rest_framework.serializers import ModelSerializer
from testapp.models import MovieInfo,Mycollection
from rest_framework.serializers import SerializerMethodField
from rest_framework.authentication import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

class Userser(ModelSerializer):
    class meta:
        model = User
        fields = '__all__'

class Movieser(ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = '__all__'

class Mycollectionser(ModelSerializer):

    class Meta:
        model = Mycollection
        fields = '__all__'

