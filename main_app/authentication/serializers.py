from rest_framework import serializers
from django.contrib.auth.models import User

import django.contrib.auth.password_validation as validators
from django.core import exceptions


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username', 'password', 'id', 'email'
            ]
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'password': {
                'write_only': True
            },
            'email': {
                'required': True
            }

        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance

    def validate(self, data):
        # user = User(**data)
        password = data.get('password')
        errors = dict() 
        try:
            validators.validate_password(password=password, user=User)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(CustomUserSerializer, self).validate(data)