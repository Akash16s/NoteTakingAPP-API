from rest_framework import serializers
from django.contrib.auth.models import User
from .models import noteModel


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "username"]


class noteSerializer(serializers.ModelSerializer):
    class Meta:
        model = noteModel
        fields = "__all__"
