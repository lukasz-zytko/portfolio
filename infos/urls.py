from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path("", lambda request: HttpResponse("Strona główna")),
    path("me", lambda request: HttpResponse("O mnie")),
    path("contact", lambda request: HttpResponse("Kontakt")),
]