from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_active(self):
        return True

    def is_staff(self):
        return False

    def has_module_perms(self, obj=None):
        return False

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

class Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_info = models.TextField(null=True, blank=True)
