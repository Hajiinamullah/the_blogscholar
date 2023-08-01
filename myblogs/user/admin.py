from django.contrib import admin
from django.contrib.admin.sites import NotRegistered

from .models import UserProfile
# Register your models here.
admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'created_at', 'updated_at')
try:
    admin.site.unregister(UserProfile)
except NotRegistered:
    pass

# Then register the model again with the custom admin class
admin.site.register(UserProfile, UserProfileAdmin)