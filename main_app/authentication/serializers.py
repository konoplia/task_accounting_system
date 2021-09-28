from rest_framework import serializers
from .models import NewUser


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = NewUser(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance
