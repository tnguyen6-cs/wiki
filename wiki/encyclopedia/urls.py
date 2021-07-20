from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("str:<entry>", views.entry, name="entry"),
]
