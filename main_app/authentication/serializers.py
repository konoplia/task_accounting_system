from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = User(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance
