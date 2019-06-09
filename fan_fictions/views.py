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
        if story.public or story.author == request.user:
            context = {
                'story': story,
                'entry': entry
            }
            return render(request, 'fan_fictions/chapter.html', context)
        else:
            raise Http404("Story isn\'t public.")
    except Story.DoesNotExist:
        raise Http404("Story does not exist")

def new_story(resquest):
    """Add a new story"""
    if resquest.method != 'POST':
        # No data submitted; create a blank form.
        form = StoryForm()
    else:
        # POST data submitted; process data.
        form = StoryForm(resquest.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fan_fictions:stories'))

    context = {'form': form}
    return render(resquest, 'fan_fictions/new_story.html', context)

def new_entry(request, story_id):
    """Add a new entry to the story"""
    story = Story.objects.get(id=story_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            # Foreign Key relationship with Story model
            new_entry.story = story
            new_entry.save()
            return HttpResponseRedirect(reverse('fan_fictions:story', args=[story_id]))
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
    context={'entry': entry, 'story': story, 'form':form}
    return render(request, 'fan_fictions/edit_entry.html', context)
