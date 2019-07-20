from django.contrib import admin
from users.models import Comment, UserProfiles
# Register your models here.

admin.site.register(Comment)
admin.site.register(UserProfiles)