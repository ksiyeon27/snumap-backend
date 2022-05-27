from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from place.models import Location, Place, Tag


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'latitude',
            'longitude'
        )
    def validate(self, data):
        return data

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name'
        )
    def validate(self, data):
        return data
        
class PlaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    number = serializers.IntegerField()
    category = serializers.IntegerField()
    type = serializers.IntegerField()
    information = serializers.CharField(max_length=500, allow_null=True)
    location = LocationSerializer(read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'number',
            'category',
            'type',
            'location',
            'information',
            'tags'
        )

    def validate(self, data):
        return data


class PlaceInRoomSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    
    class Meta:
        model = Place
        fields = (
            'id',
            'name',
            'number',
            'location'
        )