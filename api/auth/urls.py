from django.urls import path

from . import views


urlpatterns = [
    path('auth/v1/spotify/callback/',views.SpotifyOauthCallBackView.as_view(), name="oauth_callback"),
    path('auth/v1/logout/', views.LogoutView.as_view(), name="logout"),
    path('auth/v1/test/',views.ProtectedView.as_view(),name="test_endpoint"),
]