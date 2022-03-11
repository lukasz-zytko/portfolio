from django.http import HttpResponse
from django.urls import path
from .views import home, me, contact

urlpatterns = [
    path("", home),
    path("me", me),
    path("contact", contact),
]