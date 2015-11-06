from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
  # fields = ['title', 'desc', 'url', 'is_publish']
  fieldsets = [
    (None, {'fields': ['title', 'desc', 'url']}),
    ('Published', {'fields': ['is_publish']}),
  ]

admin.site.register(Blog, BlogAdmin)
