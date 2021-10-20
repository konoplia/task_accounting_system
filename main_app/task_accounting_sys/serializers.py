import logging
from rest_framework import serializers

from .models import Task

logger = logging.getLogger('info')
logger_debug = logging.getLogger('debug')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


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
            'description'
        ]
