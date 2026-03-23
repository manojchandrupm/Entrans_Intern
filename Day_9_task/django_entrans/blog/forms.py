from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
    
    """if the user enter less than 5 character it will through error"""
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title