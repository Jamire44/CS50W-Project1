from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_name>",views.visit, name="visit"),
    path("search/", views.search, name="search"),
    path("entry/", views.entry, name="entry"),
    path("<str:entry_name>/edit/", views.edit_entry, name="edit_entry"),
    path("random/", views.random_page, name="random")
]
