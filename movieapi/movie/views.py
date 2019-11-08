from django.shortcuts import render
from .models import MovieList,Watch,PopularList,LatestList#,Recommend
from .serializers import movieSerializers,watchSerializers,popularSerializers,latestSerializers
from rest_framework import viewsets , permissions
from tmdbv3api import Movie,TMDb
tmdb = TMDb()
tmdb.api_key = '48bce3138f2ee36e855fb0bde30b0d27'
tmdb.language ='en'
movie = Movie()

class movieView(viewsets.ModelViewSet):
    queryset = MovieList.objects.all()
    serializer_class = movieSerializers


class watchView(viewsets.ModelViewSet):
    queryset = Watch.objects.all()
    serializer_class = watchSerializers        

class polularView(viewsets.ModelViewSet):
    queryset = PopularList.objects.all()
    serializer_class = popularSerializers 
    #permission_classes = (permissions.IsAdminUser,)   
         

class latestView(viewsets.ModelViewSet):
    queryset = LatestList.objects.all()
    serializer_class = latestSerializers 

#class latestView(viewsets.ModelViewSet):
#	queryset = Recommend.objects.all()
