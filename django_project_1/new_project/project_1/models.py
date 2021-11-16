from django.db import models


STATUS_CHOICES = (
    (0, 'NEW'),
    (1, 'OLD'),
)


class Film(models.Model):
    name = models.CharField(max_length=200)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField()
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
