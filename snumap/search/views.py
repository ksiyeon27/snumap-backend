from itertools import chain

from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from place.models import Place
from place.serializers import PlaceSearchSerializer
from room.models import Room
from room.serializers import RoomSearchSerializer

# Create your views here.

class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request):
        keyword = request.GET.get("keyword", None)
        modelType = request.GET.get("modelType", None)
        
        places = Place.objects.all()
        rooms = Room.objects.all()
        if(keyword):
            places = places.filter(Q(name__contains=keyword)|Q(tags__name__contains=keyword)).distinct()
            rooms = rooms.filter(Q(name__contains=keyword)|Q(tags__name__contains=keyword)).distinct()
        
        data = []
        if(modelType=="room"):
            data += RoomSearchSerializer(rooms, many=True).data
        elif(modelType=="place"):
            data += PlaceSearchSerializer(places, many=True).data
        else:
            data += RoomSearchSerializer(rooms, many=True).data
            data += PlaceSearchSerializer(places, many=True).data
        return Response(data, status=status.HTTP_200_OK)