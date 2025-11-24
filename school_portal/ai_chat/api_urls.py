from django.urls import path
from . import api_views

urlpatterns = [
    path('history/', api_views.ChatHistoryAPIView.as_view(), name='api_chat_history'),
    path('send/', api_views.ChatSendAPIView.as_view(), name='api_chat_send'),
]
