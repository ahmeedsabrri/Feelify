from django.urls import path
from . import views


urlpatterns = [
    path('playlist/v1/generate/',views.GeneratePlaylist.as_view(), name="generate_playlist")
]