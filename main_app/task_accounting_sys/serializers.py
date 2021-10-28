import logging
from rest_framework import serializers
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
                raise serializers.ValidationError(f'field "{key}"  does not exist')
        return data

    def validate_executor(self, value):
        if not User.objects.get(id=value.id).groups.filter(name='Developers').exists():
            raise serializers.ValidationError("You can assign this task only to developer")
        return value


class TaskDeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'status'
        ]

    def validate(self, data):
        fields = [x for x in self.get_fields().keys()]
        for key in self.initial_data.keys():
            if key not in fields:
                raise serializers.ValidationError(f'field "{key}" does not exist')
        return data


class TaskManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'status',
            'description',
            'executor'
        ]

    def validate(self, data):
        fields = [x for x in self.get_fields().keys()]
        for key in self.initial_data.keys():
            if key not in fields:
                raise serializers.ValidationError(f'field "{key}" does not exist')
        return data

    def validate_executor(self, value):
        if not User.objects.get(id=value.id).groups.filter(name='Developers').exists():
            raise serializers.ValidationError("You can assign this task only to developer")
        return value
