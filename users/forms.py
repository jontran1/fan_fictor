from django import forms
from .models import Comment, UserProfiles

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Place Comment Here.'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class BiographyForm(forms.ModelForm):
    class Meta:
        model = UserProfiles
        fields = {'biography'}
        labels = {'biography': 'Enter bio here.'}
        widgets = {'biography': forms.Textarea(attrs={'cols': 80})}

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfiles
        fields = {'profile_picture'}
        labels = {'profile_picture': 'Link to image please.'}
