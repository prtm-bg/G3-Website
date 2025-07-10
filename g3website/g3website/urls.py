"""
URL configuration for g3website project.

This file defines the URL patterns for the Django project.
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls"))
]
