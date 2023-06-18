from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})


def login_user(request):
    auth_form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': auth_form})


def signup_user(request):
    signup_form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': signup_form})


def logout_user(request):
    logout(request)
    return redirect('/')


def about(reqeust):
    return HttpResponse("about us page")


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'main/profile.html', {})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'main/profile.html', {})

        else:
            return HttpResponse("login failed")

