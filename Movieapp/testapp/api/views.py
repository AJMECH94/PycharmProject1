from django.shortcuts import render
from testapp.models import MovieInfo,Mycollection
from testapp.api.serializers import Movieser,Mycollectionser
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView
from rest_framework.permissions import IsAdminUser

class MovieViewLC(ListCreateAPIView):
    permission_classes = [IsAdminUser,]
    serializer_class = Movieser
    queryset = MovieInfo.objects.all()

class MovieviewRUD(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser,]
    queryset = MovieInfo.objects.all()
    serializer_class = Movieser
    lookup_field = 'uid'

class UserListView(ListAPIView):
    queryset = MovieInfo.objects.all()
    serializer_class = Movieser

class UserCollection(ListAPIView):
    queryset = Mycollection.objects.all()
    serializer_class = Mycollectionser

class UserCreateView(CreateAPIView):
    queryset = Mycollection.objects.all()
    serializer_class = Mycollectionser

class UserUpdateview(RetrieveUpdateDestroyAPIView):
    queryset = Mycollection.objects.all()
    serializer_class = Mycollectionser
    lookup_field = 'id'