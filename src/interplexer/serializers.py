from rest_framework import serializers

from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'create_time', 'modify_time', 'user']
        read_only_fields = ['user']
