from django.shortcuts import render
from django.contrib.auth import get_user_model, logout
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from user.serializers import UserCreateSerializer, UserLoginSerializer


User = get_user_model()

class UserSignUpView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )

class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )

    def put(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.execute()

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserLogoutView(APIView):
    def post(self, request):
        logout(request)

        return Response({"You've been logged out"}, status=status.HTTP_200_OK)