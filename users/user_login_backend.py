from django.contrib.auth.hashers import check_password
from .models import User

class UserBackend(object):
    def authenticate(self, email=None, password=None):
        user = User.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        return User.objects.get(pk=user_id)
