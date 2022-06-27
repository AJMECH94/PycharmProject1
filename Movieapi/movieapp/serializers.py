from rest_framework.serializers import ModelSerializer
from .models import MovieInfo,Mycollection

class Movieser(ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = '__all__'

class Mycollectionser(ModelSerializer):
    class Meta:
        model = Mycollection
        fields = '__all__'