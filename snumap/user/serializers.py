from rest_framework import serializers, status

class UserCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

class UserLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)