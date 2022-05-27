from django.shortcuts import render
from rest_framework import status, viewsets
from place.models import Place
from room.models import Room
from room.serializers import RoomSerializer

# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    lookup_field = 'id'
    def get_serializer_class(self):
        return RoomSerializer