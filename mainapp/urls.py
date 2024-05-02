from . import views
from django.urls import path

urlpatterns = [
    # URL movie detail
    path("<int:movie_id>/detail/", views.detail, name="movie_detail"),
    # URL listing page
    path("home/", views.home, name="home"),
    # URL for search movie by name
    path("home/search", views.search_by_name, name="movie_name"),

    # URL add dummy data to database
    path("json_to_database/", views.json_to_database),
]


