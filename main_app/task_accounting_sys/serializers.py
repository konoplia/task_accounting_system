from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.Serializer):
    TASK_STATUS = (
        (1, 'TODO'), (2, 'READY'), (3, 'IN PROGRESS'),
        (4, 'COMPLETED')
    )

    PRIORITY = (
        (1, 'High'), (2, 'Med'), (3, 'Low')
    )

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    create_date = serializers.DateTimeField()
    status = serializers.IntegerField()
    priority = serializers.IntegerField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
