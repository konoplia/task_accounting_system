from rest_framework import serializers
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username', 'password', 'id'
            ]
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'password': {
                'write_only': True
            }

        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance
