from django.contrib import admin
from .models import blogs
from .models import Comment
admin.site.register(blogs)
admin.site.register(Comment)
# Register your models here.
class blogadmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'detail', 'post_date')