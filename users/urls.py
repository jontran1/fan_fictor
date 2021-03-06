"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = 'users'
urlpatterns = [
    # Login page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('mystories/', views.my_stories, name='my_stories'),
    path('stories/<int:story_id>/<int:entry_id>/new_comment', views.new_comment, name='new_comment'),
    path('myprofile/', views.my_profile, name='my_profile'),
    path('delete_comment/<int:story_id>/<int:entry_id>/<int:comment_id>', views.remove_comment, name='remove_comment'),
    path('myprofile/edit_bio/', views.edit_bio, name='edit_bio'),
    path('myprofile/change_profile_picture/', views.change_profile_picture, name='change_profile_picture')

]