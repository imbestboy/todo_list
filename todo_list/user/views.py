from rest_framework import generics, mixins
from . import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.SignUpSerializer
    permission_classes = []
