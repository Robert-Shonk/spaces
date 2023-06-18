from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def login_user(request):
    return HttpResponse("login page")

def signup_user(request):
    return HttpResponse("sign up page")

def about(reqeust):
    return HttpResponse("about us page")

