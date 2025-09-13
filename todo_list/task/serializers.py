from rest_framework import serializers
from . import models
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Task
        fields = ("id", "user", "title", "description", "is_done", "dead_line")
        read_only_fields = ("id", "user")

    def create(self, validated_data):
        validated_data.update({"user": self.context["user"]})
        return super().create(validated_data)
