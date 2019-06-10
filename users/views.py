from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from fan_fictions.models import Story
from django.http import Http404
from django.contrib.auth.decorators import login_required


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
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('fan_fictions:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def my_stories(request):
    """Show all stories belonging to current logged in user."""
    stories = request.user.story_set.order_by('date_added')
    context = {'stories' : stories}
    return render(request, 'fan_fictions/stories.html', context)

