from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import GeneratePlaylistSerializer, PlaylistSerializer

class GeneratePlaylist(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = GeneratePlaylistSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            playlist_obj = serializer.save()
            return Response(PlaylistSerializer(playlist_obj).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListPlaylist(APIView):
    permission_classes = [IsAuthenticated]
    pass


