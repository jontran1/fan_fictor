from django.db import models
from django.contrib.auth.models import User
from fan_fictions.models import Entry, Story
# Create your models here.


class Comment(models.Model):
    """A comment"""
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text

class UserProfiles(models.Model):
    """User's profiles"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=1000)
    profile_picture = models.CharField(max_length=1000)