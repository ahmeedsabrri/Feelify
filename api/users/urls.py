from django.urls import path

from . import views


urlpatterns = [
    path('users/v1/me',views.UserInfoView.as_view(), name="get_user"),
]