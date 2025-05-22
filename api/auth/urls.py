from django.urls import path

from . import views


urlpatterns = [
    path('auth/v1/spotify/callback/',views.SpotifyOauthCallBackView.as_view(), name="oauth_callback"),
]