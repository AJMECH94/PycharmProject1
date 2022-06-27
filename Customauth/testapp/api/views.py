from django.shortcuts import render,redirect
from testapp.models import MovieInfo,Mycollection
from testapp.api.serializers import Movieser,Mycollectionser
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,DjangoModelPermissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.contrib import auth
from rest_framework import request
from django.db.models import Prefetch
from django.contrib.auth.models import User

class MovieViewLC(ListCreateAPIView):
    permission_classes = [IsAdminUser,]
    serializer_class = Movieser
    queryset = MovieInfo.objects.all()
    pagination_class = PageNumberPagination

class MovieviewRUD(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser,]
    queryset = MovieInfo.objects.all()
    serializer_class = Movieser
    lookup_field = 'uid'


class UserListView(ListAPIView):
    queryset = MovieInfo.objects.all()
    serializer_class = Movieser

""" This view should return a list of all the purchases
    for the currently authenticated user.
"""

class UserCollection(generics.ListAPIView):
    serializer_class = Mycollectionser
    permission_classes = [AllowAny]
    #queryset = Mycollection.objects.all()

    def get_queryset(self):
        user = self.request.user
        #if user.is_active:
        return Mycollection.objects.all()
        #return None

        '''user = User.objects.all()
        queryset = user.prefetch_related(Prefetch('uid_set',queryset=Mycollection.objects.filter(user_id__in=user)))
        return queryset'''';h '


'''
class UserCollection(ListAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    queryset = Mycollection.objects.all()
    serializer_class = Mycollectionser'''


class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    #authentication_classes = [JSONWebTokenAuthentication]
    queryset = Mycollection.objects.all()
    serializer_class = Mycollectionser


class UserUpdateview(RetrieveUpdateDestroyAPIView):
   # authentication_classes = [JSONWebTokenAuthentication]
    queryset = Mycollection.objects.all()
    serializer_class = Mycollectionser
    lookup_field = 'id'
