from django import forms
from .models import Post, Message

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['author', 'content']