from django import forms
from .models import Story, Entry

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'public', 'story_cover']
        labels = {'title': 'Title:', 'public': True, 'story_cover': 'Story cover'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
        labels = {'title:': 'Title:', 'text': 'Chapter:'}
        # By telling django to use forms.Textarea element,
        # we are customizing the input widget for the field 'text
        # 80 will give us 80 columns wide, enough for a user to input text.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}