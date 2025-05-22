from django.shortcuts import render
from users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SpotifyOauthCallBackSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
# Create your views here.


class SpotifyOauthCallBackView(APIView):
    permission_classes = []
    serializer_class = SpotifyOauthCallBackSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response = Response({
            "message": "You logged in successfully",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        
        return response