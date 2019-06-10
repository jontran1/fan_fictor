from django.urls import path
from . import views

app_name = 'fan_fictions'
urlpatterns = [
    path('', views.index, name='index'),
    path('stories/', views.stories, name='stories'),
    path('stories/<int:story_id>/', views.story, name='story'),
    path('stories/<int:story_id>/<int:entry_id>', views.chapter, name='chapter'),
    path('stories/new_story/', views.new_story, name='new_story'),
    path('stories/<int:story_id>/new_entry', views.new_entry, name='new_entry'),
    path('stories/edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    path('stories/edit_story/<int:story_id>', views.edit_story, name='edit_story'),
]