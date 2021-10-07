from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    STATUS = (
        (1, 'TO DO'),
        (2, 'IN PROGRESS'),
        (3, 'READY'),
        (4, 'COMPLETED'),
    )

    status = serializers.ChoiceField(choices=STATUS)

    class Meta:
        model = Task
        fields = '__all__'
         #   [
        #     'id', 'name', 'description', 'create_date', 'status', 'priority', 'created_by', 'executor'

        #]
