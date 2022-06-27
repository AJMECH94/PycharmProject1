from django.shortcuts import render
from django.template.base import Token
from rest_framework.views import APIView
from .serializer import Userserializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
class RegisterUser(APIView):
    authentication_classes = [TokenAuthentication,]
    #serializer_class = [Userserializer,]
    def post(self,request):
        ser = Userserializer(data=request.data)

        if not ser.is_valid():
            print(ser.errors)
            return Response({'status':403,'errors':ser.errors})

        ser.save()

        #user = User.objects.get(username=ser.data['username'])
        #token_obj, _ = Token.objects.get_or_create(user=user)

        return Response({'status':200,'payload':ser.data,'token':str(token_obj)})