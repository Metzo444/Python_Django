from django.db import models
from helpers.choices import STATUS_CHOICES_1


class Film(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=256)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_punlished = models.BooleanField()
    status = models.IntegerField(choices=STATUS_CHOICES_1)

    def __str__(self):
        return self.name
