from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import video
from threading import Thread
from .serializer import VideoViewSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework_api_key.permissions import HasAPIKey
from asgiref.sync import sync_to_async
from time import sleep
# Create your views here.


#index page dummy!
def index(request):
    return HttpResponse("HELLO")

#CLASS Viewset for custom designed API
class VideoViewset(viewsets.ReadOnlyModelViewSet):
    queryset = video.objects.all().order_by('-publishedAt') #listing of video in reverse chronological order
    serializer_class = VideoViewSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [HasAPIKey]
    search_fields = ['title', 'description','tags']
    def get_queryset(self):
        queryset = video.objects.all().order_by('-publishedAt')
        if self.request.query_params.get('id') is not None:
            id=self.request.query_params.get('id')
            queryset = video.objects.all().filter(id=id).order_by('-publishedAt')
        if self.request.query_params.get('tag') is not None:
            tag=self.request.query_params.get('tag')
            tobedel=[]
            for v in queryset:
                if tag not in list(v.tags):
                    tobedel.append(v.id)
            queryset=video.objects.exclude(id__in=tobedel)
        return queryset


#the view function to load video from 
# youtube API and store in database
def LoadVideos(request):
    print("API Called")
    API="https://www.googleapis.com/youtube/v3/videos?key=AIzaSyDfp7FLcYI_KurONqXpPgcAb1TJ-PcSdCw&fields=(items(id,snippet(title,description,tags,thumbnails,publishedAt)),nextPageToken)&part=snippet&chart=mostPopular&maxResults=50&type=video&regionCode=IN"
    result=requests.get(API).json()
    for item in result['items']:
        try:
            v=video.objects.get(id=item['id'])
            continue
        except:
            v=video()
            v.id=item['id']
            v.title=item['snippet']['title']
            v.description=item['snippet']['description']
            v.thumbnail=item['snippet']['thumbnails']['default']['url']
            v.publishedAt=item['snippet']['publishedAt']
            try:
                v.tags=item['snippet']['tags']
            except:
                v.tags=[]
            v.save()
       #making the function call after every 10 sec
    return HttpResponse("Video Loaded")

