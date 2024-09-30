from django.contrib.auth.models import User
from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"Feedback from {self.user.username if self.user else 'Anonymous'}"
# Create your models here.
