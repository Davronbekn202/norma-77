from django import forms
from .models import Contact, Post


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']