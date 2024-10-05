"""
Route path for Shotener App
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShrinkLink.as_view()),
    path("<myhash>", views.ShrinkLink.as_view())
]
