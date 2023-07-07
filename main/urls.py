from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name='login_user'),
    path('signup/', views.signup_user, name='signup_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('createspace/', views.create_space, name='create_space'),
    path('space/<str:spacename>/', views.space, name='space'),
    path('space/<str:spacename>/post/', views.post, name='post'),
    path('space/<str:spacename>/comments/<str:post_title>/', views.post_comments, name='post_comments'),
    path('space/<str:spacename>/post/delete_post/<str:post_title>/', views.delete_post, name='delete_post'),
]

