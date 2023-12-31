from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class UserFollowedSpace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spacename = models.CharField(max_length=25)

    def __str__(self):
        return self.spacename


class Space(models.Model):
    spacename = models.CharField(max_length=25)

    def __str__(self):
        return self.spacename


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    spacename = models.CharField(max_length=25)
    url = models.CharField(max_length=200, default="", blank=True)
    body = models.CharField(max_length=1000, default="")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    helpful = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    date_published = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.title


class PostUpvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=25)


class PostDownvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=25)


class PostFunny(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=25)


class PostHelpful(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=25)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    parent_comment = models.CharField(max_length=1000, default="", blank=True)
    username = models.CharField(max_length=12)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    helpful = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    date_published = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.comment


class Moderator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    head_mod = models.BooleanField(default=False)
    spacename = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username

