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

]