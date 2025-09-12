from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ("title", "description", "dead_line")

    def create(self, validated_data):
        validated_data.update({"user": self.context["user"]})
        return super().create(validated_data)
