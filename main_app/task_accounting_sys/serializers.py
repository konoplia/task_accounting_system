from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=100)
    # description = serializers.CharField(max_length=200)
    # create_date = serializers.CharField(read_only=True)
    # status = serializers.IntegerField()
    # priority = serializers.IntegerField()
    # created_by = serializers.IntegerField(read_only=True)
    class Meta:
        # import pdb
        # pdb.set_trace()
        model = Task
        fields = [
            'id', 'name', 'description', 'create_date', 'status', 'priority', 'created_by'
        ]
        # extra_kwargs = {
        #     'id': {'read_only': True},
        #     'create_data': {'read_only': True},
        #     'created_by': {'read_only': True}
        # }

    # def save(self, **kwargs):
    #
    #     import pdb
    #     pdb.set_trace()

    # def create(self, validated_data):
    #     print("2")
    #     print(validated_data)
    #     import pdb
    #     pdb.set_trace()
    #     # user = self.context['request'].user
    #     # validated_data[]
    #     return Task.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance
