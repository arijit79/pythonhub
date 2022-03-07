from django.db import models

# Create your models here.
class Unit(models.Model):
    title = models.CharField(max_length=128)
    template_dir = models.CharField(max_length=16, blank=True)

    def save(self, *args, **kwargs):
        self.template_dir = f"units/unit{self.id}/"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=256)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    s_no = models.IntegerField(verbose_name="S. No.", )
    template = models.CharField(max_length=32)

    def __str__(self):
        return self.title
