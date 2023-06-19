from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm


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
        return render(request, 'main/profile.html', {'username': username})

