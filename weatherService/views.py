from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from api.serializers import WeatherModelSeralizer
from django.conf import settings
# Create your views here.
class ScrapeView(generics.GenericAPIView):
    def get(self, request, format=None):
        #on launche eul'scrape
        return None

