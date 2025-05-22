from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SpotifyOauthCallBackSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": "You are authenticated!"})
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