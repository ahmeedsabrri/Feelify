from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.URLField()
    spotify_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
    def __str__(self):
        return self.username


class playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    spotify_id = models.CharField(max_length=128)
    playlist_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.playlist_name} ({self.user.username})"