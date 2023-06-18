from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name='login_user'),
    path('signup/', views.signup_user, name='signup_user'),
    path('about/', views.about, name='about'),
]

