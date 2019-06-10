from django.db import models
from django.contrib.auth.models import User
from fan_fictions.models import Entry
# Create your models here.


class Comment(models.Model):
    """A comment"""
    reply = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text
