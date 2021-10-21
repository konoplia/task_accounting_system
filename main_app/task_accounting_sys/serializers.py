import logging
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Task, User

logger = logging.getLogger('info')
logger_debug = logging.getLogger('debug')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        fields = [x for x in self.get_fields().keys()]
        for key in self.initial_data.keys():
            if key not in fields:
                raise serializers.ValidationError(f'field "{key}" dosen`t exist')
        return data

    def validate_executor(self, value):
        if value == self.context:
            raise serializers.ValidationError("you cannot assign the task to yourself")
        elif value > len(User.objects.all()):
            raise serializers.ValidationError("this user not exist")
        return value


class TaskDeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'status'
        ]


class TaskManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'status',
            'description',
            'executor'
        ]

    def validate_executor(self, value):
        if value == self.context:
            raise serializers.ValidationError("you cannot assign the task to yourself")
        elif value > len(User.objects.all()):
            raise serializers.ValidationError("this user not exist")
        return value
