from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
# from .models import Note
# from .serializers import NoteSerializer
from api import serializers
# Create your views here.
from .models import User, MovieCllecReady, MovieTop, RatingList, MovieURL
from .serializers import UserSerializer, MovieCllecReadySerializer, MovieTopSerializer, RatingListSerializer, MovieURLSerializer


@api_view(['GET'])
def getUserInfo(request, pk):
    info = User.objects.get(userId=pk)
    serializer = UserSerializer(info)
    return Response(serializer.data)


@api_view(['GET'])
def getCollection(request, pk):
    info = MovieCllecReady.objects.filter(userId=pk,is_collect=True)
    serializer = MovieCllecReadySerializer(info,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTowatch(request, pk):
    info = MovieCllecReady.objects.filter(userId=pk, is_towatch=True)
    serializer = MovieCllecReadySerializer(info, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMovieinfo(request, pk):
    info = MovieURL.objects.get(movieId=pk)
    serializer = MovieURLSerializer(info, many=False)
    return Response(serializer.data)

