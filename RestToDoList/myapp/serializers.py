from rest_framework import serializers
from .models import Todolist, User


class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ['id', 'title', 'created_at', 'updated_at', 'description', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
