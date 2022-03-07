from django.db import models
from users.models import User

# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    actual_answer = models.TextField(null=True, blank=True)

class Answer(models.Model):
    VALID_KEYS = (
        ("C", "Correct"),
        ("I", "Incorrect"),
    )
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid = models.CharField(max_length=1, choices=VALID_KEYS, blank=True, null=True)
