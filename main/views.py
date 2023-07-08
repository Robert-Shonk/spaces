from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm, CreateSpaceForm, PostForm, CommentForm
from .models import Space, UserFollowedSpace, Post, Comment
import datetime


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        base_template = "./loggedin_base.html"
    else:
        base_template = "./base.html"
    return render(request, 'main/index.html', {'base_template': base_template})


def login_user(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main:profile')

        else:
            return HttpResponse("incorrect info")

    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def signup_user(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login_user')

    form = CreateUserForm()
    return render(request, 'main/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')


def about(reqeust):
    return HttpResponse("about us page")


def profile(request):
    if request.user.is_authenticated:
        username = request.user
        spaces = Space.objects.all()
        followed_spaces = request.user.userfollowedspace_set.all()
        return render(request, 'main/profile.html', {'username': username, 'spaces': spaces, 'followed_spaces': followed_spaces})


def create_space(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = CreateSpaceForm(request.POST)

            if form.is_valid():
                # if true add to space table and moderator table. also need to check if spacename exists already.
                spacename = form.cleaned_data['spacename']
                try:
                    spaces = Space.objects.get(spacename=spacename)
                except Space.DoesNotExist:
                    new_space = Space(spacename=spacename)
                    new_space.save()
                    request.user.moderator_set.create(head_mod=True, spacename=spacename)
                    return redirect('main:profile')

        form = CreateSpaceForm()

        return render(request, 'main/createspace.html', {'form': form})


# still Need to update UserFollowedSpace
def space(request, spacename):

    if request.method == 'POST':
        follow_status = request.POST['followed']
        if follow_status == 'False':
            try:
                followed_space = request.user.userfollowedspace_set.get(spacename=spacename)
                followed_space.delete()
                return redirect('main:space', spacename)
            except UserFollowedSpace.DoesNotExist:
                pass
        else:
            try:
                followed_space = request.user.userfollowedspace_set.get(spacename=spacename)
            except UserFollowedSpace.DoesNotExist:
                request.user.userfollowedspace_set.create(spacename=spacename)
                return redirect('main:space', spacename)

    space_posts = Post.objects.filter(spacename=spacename)

    try:
        followed_space = request.user.userfollowedspace_set.get(spacename=spacename)
        followed = 'True'
    except UserFollowedSpace.DoesNotExist:
        followed = 'False'

    return render(request, 'main/space.html', {'spacename': spacename, 'followed': followed, 'space_posts': space_posts})


def post(request, spacename):

    if request.method == 'POST':

        try:
            post_exists = request.user.post_set.get(title=request.POST['title'])
        except Post.DoesNotExist:
            request.user.post_set.create(title=request.POST['title'], spacename=spacename,
                                         url=request.POST['url'], body=request.POST['body'])
            return redirect('main:space', spacename)

    form = PostForm()
    return render(request, 'main/post.html', {'form': form, 'spacename': spacename})


def post_comments(request, spacename, post_title):

    if request.method == 'POST':
        comment = request.POST['comment']
        username = request.user
        post_info = Post.objects.get(title=post_title)
        post_info.comment_set.create(comment=comment, username=username)
        return redirect('main:post_comments', spacename, post_title)

    post_info = Post.objects.get(title=post_title)
    comments = post_info.comment_set.all()

    comment_form = CommentForm()

    return render(request, 'main/comment.html', {'post_info': post_info, 'comments': comments,
                                                 'comment_form': comment_form})


def delete_post(request, spacename, post_title):

    if request.method == 'POST':

        try:
            post = Post.objects.get(title=post_title)
            post.delete()
            return redirect('main:space', spacename)
        except Post.DoesNotExist:
            pass

    return HttpResponse("hehe")


def delete_comment(request, spacename, post_title, comment):

    if request.method == 'POST':

        try:
            post = Post.objects.get(title=post_title)
            del_comment = post.comment_set.get(comment=comment)
            del_comment.delete()
            return redirect('main:post_comments', spacename, post_title)
        except Post.DoesNotExist:
            pass
    return HttpResponse("delete_comment")


def upvote(request, post_title):

    if request.method == "POST":

        try:
            post = Post.objects.get(title=post_title)
            post.upvotes += 1
            post.save()
            return redirect('main:post_comments', post.spacename, post_title)
        except Post.DoesNotExist:
            pass

    return HttpResponse("upvote")


def downvote(request, post_title):

    if request.method == "POST":

        try:
            post = Post.objects.get(title=post_title)
            post.downvotes += -1
            post.save()
            return redirect('main:post_comments', post.spacename, post_title)
        except Post.DoesNotExist:
            pass
    return HttpResponse("downvote")


def funny(request, post_title):
    if request.method == "POST":

        try:
            post = Post.objects.get(title=post_title)
            post.funny += 1
            post.save()
            return redirect('main:post_comments', post.spacename, post_title)
        except Post.DoesNotExist:
            pass
    return HttpResponse("funny")


def helpful(request, post_title):
    if request.method == "POST":

        try:
            post = Post.objects.get(title=post_title)
            post.helpful += 1
            post.save()
            return redirect('main:post_comments', post.spacename, post_title)
        except Post.DoesNotExist:
            pass
    return HttpResponse("helpful")

