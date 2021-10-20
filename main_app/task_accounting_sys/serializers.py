import logging
from rest_framework import serializers

from .models import Task

logger = logging.getLogger('info')
logger_debug = logging.getLogger('debug')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     logger_debug.debug(instance)
    #     logger.info(instance)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance


class TaskUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'description',
            'status'
        ]
