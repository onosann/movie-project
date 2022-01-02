from .models import User, MovieCllecReady, MovieTop, RatingList, MovieURL
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'


class MovieCllecReadySerializer(ModelSerializer):
    class Meta:
        model = MovieCllecReady
        fields = '__all__'


class MovieTopSerializer(ModelSerializer):
    class Meta:
        model = MovieTop
        fields = '__all__'


class RatingListSerializer(ModelSerializer):
    class Meta:
        model = RatingList
        fields = '__all__'
        

class MovieURLSerializer(ModelSerializer):
    class Meta:
        model = MovieURL
        fields = '__all__'
