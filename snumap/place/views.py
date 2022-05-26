from django.shortcuts import render
from rest_framework import status, viewsets
from place.models import Place
from place.serializers import PlaceSerializer

# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    lookup_field = 'id'
    def get_serializer_class(self):
        return PlaceSerializer

