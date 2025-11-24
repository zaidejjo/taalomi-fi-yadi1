from rest_framework import serializers
from .models import ChatHistory

class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['id', 'user', 'message', 'sender', 'timestamp']
        read_only_fields = ['user', 'timestamp']
