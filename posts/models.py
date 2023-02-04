from django.db import models
from django.contrib.auth.models import User
from base.models import WebUser


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post_body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duplicate_post = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def __str__(self):
        return self.post_body