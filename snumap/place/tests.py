from django.test import TestCase
from rest_framework import status
from factory.django import DjangoModelFactory

from .models import Location, Tag, Place


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location
        
class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag
        
class PlaceFactory(DjangoModelFactory):
    class Meta:
        model = Place

# Create your tests here.
