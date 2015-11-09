from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'url', 'votes', 'desc', 'is_publish')
