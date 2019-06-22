from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Story, Entry
from django.http import Http404
from .forms import StoryForm, EntryForm
# Create your views here.

def index(request):
    return render(request, 'fan_fictions/index.html')

@login_required
def stories(request):
    """Show all stories public stories"""
    stories = Story.objects.order_by('date_added').filter(public=True)
    context = {'stories': stories}
    return render(request, 'fan_fictions/stories.html', context)

@login_required
def story(request, story_id):
    """Show details of a story which is a Fan_fiction"""
    try:
        story = Story.objects.get(id=story_id)
        entries = story.entry_set.order_by('date_added')
        if story.public or story.author == request.user:
            context = {
                'story': story,
                'entries': entries
            }
            return render(request, 'fan_fictions/story.html', context)
        else:
            raise Http404("Story isn\'t public.")
    except Story.DoesNotExist:
        raise Http404("Story does not exist")


@login_required
def chapter(request, story_id, entry_id):
    """Shows the chapter of the story"""
    try:
        story = Story.objects.get(id=story_id)
        entry = Entry.objects.get(id=entry_id)
        comments = entry.comment_set.order_by('-date_added')
        if story.public or story.author == request.user:
            context = {
                'story': story,
                'entry': entry,
                'comments': comments,
            }
            return render(request, 'fan_fictions/chapter.html', context)
        else:
            raise Http404("Story isn\'t public.")
    except Story.DoesNotExist:
        raise Http404("Story does not exist")

@login_required
def new_story(request):
    """Add a new story"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = StoryForm()
    else:
        # POST data submitted; process data.
        form = StoryForm(request.POST)
        if form.is_valid():
            new_story = form.save(commit=False)
            new_story.author = request.user
            new_story.save()
            return HttpResponseRedirect(reverse('fan_fictions:stories'))

    context = {'form': form}
    return render(request, 'fan_fictions/new_story.html', context)

@login_required
def new_entry(request, story_id):
    """Add a new entry to the story"""
    story = Story.objects.get(id=story_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid() and request.user == story.author:
            new_entry = form.save(commit=False)
            # Foreign Key relationship with Story model
            new_entry.story = story
            new_entry.author = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('fan_fictions:story', args=[story_id]))
        else:
            raise Http404("You are not the owner of this story.")
    context = {'story': story, 'form': form}
    return render(request, 'fan_fictions/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    story = entry.story

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fan_fictions:chapter', args=[story.id, entry.id]))
    context={'entry': entry, 'story': story, 'form': form}
    return render(request, 'fan_fictions/edit_entry.html', context)

def edit_story(request, story_id):
    """Edit an existing story"""
    story = Story.objects.get(id=story_id)
    entries = story.entry_set.order_by('date_added')

    if request.method != 'POST':
        form = StoryForm(instance=story)
    else:
        form = StoryForm(instance=story, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fan_fictions:story', args=[story_id]))
    context = {'story': story, 'entries': entries, 'form': form}

    return render(request, 'fan_fictions/edit_story.html', context)