from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add_category, name='add_category')
]