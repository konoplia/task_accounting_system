from rest_framework import serializers
from .models import NewUser


class CustomUserSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = NewUser(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
