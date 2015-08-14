from django.db import models
from django.utils import timezone


class Accomplishment(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text