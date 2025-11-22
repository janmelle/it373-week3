from django import forms
from pages.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['title', 'body',]
        # exclude = ['title',]