from django import forms
from .models import Post

class uploadForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'created_on']
