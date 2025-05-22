from rest_framework import serializers
import requests
from users.models import User


class SpotifyOauthCallBackSerializer(serializers.Serializer):
    code = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        code = attrs.get('code')
        
        response = requests.post(
            'https://accounts.spotify.com/api/token',
            data={
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': 'http://127.0.0.1:8000/api/auth/v1/spotify/callback/',
                'client_id': '72a78c714b824bf090833a060f838045',
                'client_secret': '1918fed7b7134af786d8e34e9d2c7e97',
            }
        )
        if response.status_code != 200:
            raise serializers.ValidationError('Failed to get access token from Spotify.')
        access_token = response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        user_response = requests.get('https://api.spotify.com/v1/me', headers=headers)
        if response.status_code != 200:
            raise serializers.ValidationError('Invalid or expired Spotify access token.')
        data = user_response.json()
        avatar_url = data["images"][0]["url"] if data.get("images") and len(data["images"]) > 0 else ""
        attrs['username'] = data["display_name"]
        attrs['email'] = data["email"]
        attrs['avatar'] = avatar_url
        return attrs
    def create(self, validated_data):
        user, _ = User.objects.get_or_create(
            username=validated_data['username'],
            defaults={
                'email':validated_data['email'],
                'avatar':validated_data['avatar']
            }
        )
        return user