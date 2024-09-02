from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_name>",views.visit, name="visit"),
    path("search/", views.search, name="search"),
    path("entry/", views.entry, name="entry")
]
