from django.urls import path
from . import views

urlpatterns = [

    path("", views.add_anime),
    path("anime/new", views.newAnime),
    path("fans", views.add_fans),
    path("fans/new", views.newFans),
    path("anime/<int:anime_id>", views.anime_list),
    path("fans_list/<int:fans_id>", views.fans_list)
]