from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


# new Authentication backend to support both email and username signin
class AuthenticationModelBackend(ModelBackend):
    # change only authenticate method to support email and username signin
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user and user.check_password(password):
            return user
        return None
