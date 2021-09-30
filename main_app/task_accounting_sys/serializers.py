from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    create_date = serializers.CharField(read_only=True)
    status = serializers.IntegerField()
    priority = serializers.IntegerField()
    create_by = serializers.CharField(read_only=True)

    def create(self, validated_data):
        import pdb
        pdb.set_trace()
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
