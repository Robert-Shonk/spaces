from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Textarea
from .models import Post


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateSpaceForm(forms.Form):
    spacename = forms.CharField(label="Space name", max_length=25)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'url', 'body']
        widgets = {
            'body': Textarea(attrs={'cols': 80, 'rows': 20})
        }
