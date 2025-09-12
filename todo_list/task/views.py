from django.contrib.auth import get_user_model
from rest_framework import viewsets
from . import models
from . import serializers

User = get_user_model()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return models.Task.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
