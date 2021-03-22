from django.shortcuts import render, redirect
from .models import Anime, Fans

def add_anime(request):
    context = {"all_anime": Anime.objects.all()}
    return render(request, "add_anime.html", context)

def newAnime(request):
    print(request.POST)
    new_anime = Anime.objects.create(
        title = request.POST["title"],
        desc = request.POST["desc"]
    )
    return redirect("/")

def add_fans(request):
    context = {"fans": Fans.objects.all()}
    return render(request, "fans.html", context)


def anime_list(request, anime_id):
    context = {
        "liked_anime" : Anime.objects.get(id=anime_id),
        "the_fans" : Fans.objects.all(),
    }
    return render(request, "animes.html", context)

def fans_list(request, fans_id):
    context = {
        "the_fans" : Fans.objects.get(id=fans_id),
        "liked_anime" : Anime.objects.all()
    }
    return render(request, "fans_list.html", context)

def newFans(request):
    print(request.POST)
    new_fan = Fans.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        notes = request.POST["notes"]
    )
    return redirect("/fans")