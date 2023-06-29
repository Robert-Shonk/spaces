from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Textarea
from .models import Post, Comment


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateSpaceForm(forms.Form):
    spacename = forms.CharField(label="Space name", max_length=25)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'spacename', 'url', 'body']
        widgets = {
            'user': forms.HiddenInput(),
            'spacename': forms.HiddenInput(),
            'body': Textarea(attrs={'cols': 80, 'rows': 20})
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'comment', 'parent_comment', 'username']