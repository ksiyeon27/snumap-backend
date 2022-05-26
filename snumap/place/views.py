from django.shortcuts import render
from rest_framework import status, viewsets
from place.models import Place
from place.serializers import PlaceSerializer
from room.serializers import RoomInPlaceSerializer
from room.models import Room
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action

# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    lookup_url_kwarg = 'place_id'
    def get_serializer_class(self):
        if self.action in ['rooms']:
            return RoomInPlaceSerializer
        return PlaceSerializer

    def get_queryset(self):
        queryset = Place.objects.all()
        if self.action in ['rooms']:
            self.place = getattr(self, 'place', None) or get_object_or_404(queryset, pk=self.kwargs[self.lookup_url_kwarg])
            queryset = self.place.rooms

        return queryset

    @action(detail=True)
    def rooms(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    