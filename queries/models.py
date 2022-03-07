from django.db import models
from users.models import User

# Create your models here.
class Query(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    answer = models.TextField(null=False, blank=True)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Query"
        verbose_name_plural = "Queries"
