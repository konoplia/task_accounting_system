from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    # password = serializers.CharField(max_length=100)
    # class Meta:
    #     model = User
    #     fields = ['id', 'name', 'email', 'password']
    #
    #     extra_kwargs = {
    #         'password': {'write_only': True}
    #     }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = User(**validated_data)
        if password is not None:
            instance.set_password(password)
        print('1')
        return instance
        # return User.objects.create(**validated_data)
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     import pdb
    #     pdb.set_trace()
    #     if password is not None:
    #         instance.set_password(password)
    #     return instance
