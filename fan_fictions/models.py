from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    title = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    story_cover = models.URLField()

    class Meta:
        verbose_name_plural = 'stories'

    def __str__(self):
        return self.title

class Entry(models.Model):
    """A fan fiction story"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    chapter_cover = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text
