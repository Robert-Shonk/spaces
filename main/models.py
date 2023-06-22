from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserFollowedSpaces(models.Model):
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
    url = models.CharField(max_length=200, default="")
    body = models.CharField(max_length=1000, default="")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    helpful = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    username = models.CharField(max_length=12)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    helpful = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.comment


class Moderator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    head_mod = models.BooleanField(default=False)
    spacename = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username

