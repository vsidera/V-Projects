from django import forms
from .models import Post , Rating

class uploadForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'created_on']

class ratingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['interface', 'experience', 'content']        
