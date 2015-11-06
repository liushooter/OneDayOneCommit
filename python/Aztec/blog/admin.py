from django.contrib import admin
from .models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'desc', 'url']

admin.site.register(Blog, BlogAdmin)
