from django.db import models
from base.models import WebUser


class Post(models.Model):
    author = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    post_body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def __str__(self):
        return self.post_body