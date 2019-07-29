from django.shortcuts import render
# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from fan_fictions.models import Story, Entry
from users.models import UserProfiles, Comment
from .forms import CommentForm, BiographyForm
from django.http import Http404



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('fan_fictions:index'))

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page
            # When they register, the user is asked to enter two
            # matching passwords, and because the form is valid, we know the passwords
            # match so we can use either one. Here we get the value associated with the
            # 'password1' key in the form’s POST data.
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            user_profile = UserProfiles(user=authenticated_user,
                                        biography='Nothing yet...',
                                        profile_picture='https://i.imgur.com/ZfgGvCL.png')
            user_profile.save()
            login(request, authenticated_user)

            return HttpResponseRedirect(reverse('fan_fictions:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def my_stories(request):
    """Show all stories belonging to current logged in user."""
    stories = request.user.story_set.order_by('date_added')
    context = {'stories': stories}
    return render(request, 'fan_fictions/my_stories.html', context)

@login_required
def new_comment(request, story_id, entry_id):
    """Add a new comment"""
    story = Story.objects.get(id=story_id)
    entry = Entry.objects.get(id=entry_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            # Foreign Key relationship
            new_comment.story = story
            new_comment.entry = entry
            new_comment.user = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('fan_fictions:chapter', args=[story_id, entry_id]))

    context = {'story': story,
               'entry': entry,
               'form': form}
    return render(request, 'users/new_comment.html', context)

@login_required
def remove_comment(request, story_id, entry_id, comment_id):
    if request.user == story_id.author:
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return HttpResponseRedirect(reverse('fan_fictions:chapter', args=[story_id, entry_id]))
    else:
        raise Http404("You are not authorized to remove comment.")


@login_required
def my_profile(request):
    """Displays the profile.html file."""
    user = request.user
    user_profile = UserProfiles.objects.get(user=user)
    stories = user.story_set.order_by('-date_added')

    context = {'user': user,
               'user_profile': user_profile,
               'stories': stories
               }
    return render(request, 'users/profiles.html', context)

@login_required
def edit_bio(request):
    """Edit an existing bio of the currently logged in user."""
    users_profile = UserProfiles.objects.get(user=request.user)
    if request.user != users_profile.user:
        raise Http404("You do not have permission")
    if request.method != 'POST':
        form = BiographyForm(instance=users_profile)
    else:
        form = BiographyForm(instance=users_profile, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:my_profile'))

    context = {'form': form}
    return render(request, 'users/edit_bio.html', context)

def users_profiles(request, user_id):
    return render(request, 'users/profiles.html')

