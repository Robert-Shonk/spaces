from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm, CreateSpaceForm
from .models import Space


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})


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
        return render(request, 'main/profile.html', {'username': username, 'spaces': spaces})


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
        followed = request.POST['followed']
    else:
        followed = 'False'

    return render(request, 'main/space.html', {'spacename': spacename, 'followed': followed})

