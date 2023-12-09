from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    # path('logout/', views.user_logout, name='user_logout'),
    path('logout/', views.LogoutView.as_view(), name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/edit/pass_change/', views.pass_change, name='pass_change'),
]