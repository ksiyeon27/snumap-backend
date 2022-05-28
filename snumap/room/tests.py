from django.test import TestCase
from rest_framework import status
from factory.django import DjangoModelFactory

from .models import Room

class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room
