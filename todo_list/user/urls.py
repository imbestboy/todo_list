from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path("signin/", TokenObtainPairView.as_view()),
    path("signup/", views.SignUpAPIView.as_view()),
]
