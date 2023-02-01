from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# # สร้าง WebUser object เมื่อมีการ create user
# @receiver(post_save, sender=User)
# def create_user_picks(sender, instance, created, **kwargs):
#     if created:
#         WebUser.objects.create(_user=instance)

# Create your models here.
class WebUser(User):
    name = models.CharField(blank=True, max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.username

    