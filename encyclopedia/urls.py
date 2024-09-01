from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_name>",views.visit, name="visit"),
    path("search/", views.search, name="search"),  # Add this line for search functionality
    path("new_entry/", views.create_new_entry, name="new_entry")
]
