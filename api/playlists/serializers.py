from rest_framework import serializers
from users.models import playlist, Track
from .utils.generate import get_playlist_tracks_from_ai

class GeneratePlaylistSerializer(serializers.Serializer):
    mood = serializers.CharField(required=True)
    genres = serializers.ListField(child=serializers.CharField(), required=True)
    artists = serializers.ListField(child=serializers.CharField(), required=False)
    playlist_name = serializers.CharField(required=True)
    num_tracks = serializers.IntegerField(default=20)
    description = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        tracks = get_playlist_tracks_from_ai(
            mood=attrs['mood'],
            genres=attrs['genres'],
            artists=attrs.get('artists', []),
            playlist_name=attrs['playlist_name'],
            num_tracks=attrs['num_tracks']
        )
        attrs['tracks'] = tracks
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        playlist_obj = playlist.objects.create(
            user=user,
            spotify_id=user.spotify_id,
            playlist_name=validated_data['playlist_name'],
            description=validated_data.get('description', ''),
        )
        for track in validated_data['tracks']:
            Track.objects.create(
                playlist=playlist_obj,
                name=track['track'],
                artist=track['artist']
            )
        return playlist_obj

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['name', 'artist']

class PlaylistSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = playlist
        fields = ['id', 'playlist_name', 'description', 'created_at', 'tracks']