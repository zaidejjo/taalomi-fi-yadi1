from django.urls import path
from . import api_views

urlpatterns = [
    path('auth/login/', api_views.LoginAPIView.as_view(), name='api_login'),
    path('auth/logout/', api_views.LogoutAPIView.as_view(), name='api_logout'),
    path('auth/user/', api_views.UserAPIView.as_view(), name='api_user'),
    path('dashboard/', api_views.DashboardAPIView.as_view(), name='api_dashboard'),
]
