from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class WebUser(User):
    name = models.CharField(blank=True, max_length=255)
    # friend

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.username

    