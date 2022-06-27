from django.shortcuts import render
from .models import MovieInfo,Mycollection
from .serializers import Movieser,Mycollectionser
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView


class MovieViewLC(ListCreateAPIView):
    serializer_class = Movieser
    queryset = MovieInfo.objects.all()

class MovieviewRUD(RetrieveUpdateDestroyAPIView):
    queryset = MovieInfo.objects.all()
    serializer_class = Movieser
    lookup_field = 'uid'

class UserListView(ListAPIView):
    queryset = MovieInfo.objects.all()
    serializer_class = Movieser

class UserCreateView(CreateAPIView):
    queryset = Mycollection.objects.all()
    serializer_class = Mycollectionser

class UserUpdateview(RetrieveUpdateDestroyAPIView):
    queryset = Mycollection.objects.all()
    serializer_class = Mycollectionser
    lookup_field = 'id'