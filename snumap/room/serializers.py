from rest_framework import serializers, status
from place.models import Place
from room.models import Room
from place.serializers import TagSerializer, PlaceInRoomSerializer

class RoomInPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'number',
            'type'
        )

    def validate(self, data):
        return data

class RoomSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    number = serializers.IntegerField()
    type = serializers.IntegerField()
    floor = serializers.IntegerField()
    building = PlaceInRoomSerializer()
    information = serializers.CharField(max_length=500, allow_null=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'number',
            'type',
            'floor',
            'building',
            'information',
            'tags'
        )

    def validate(self, data):
        return data
    
class RoomSearchSerializer(serializers.ModelSerializer):
    modelType = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'modelType'
        )
        
    def get_modelType(self, room):
        return "room"