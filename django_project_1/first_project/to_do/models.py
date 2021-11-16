from django.db import models
# from helpers.choices import STATUS_CHOICES_1
from helpers.choices import STATUS_CHOICES


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Film(models.Model):
#     DoesNotExist = None
#     objects = None
#     name = models.CharField(max_length=256)
#     rate = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_punlished = models.BooleanField()
#     status = models.IntegerField(choices=STATUS_CHOICES_1)
#
#     def __str__(self):
#         return self.name
