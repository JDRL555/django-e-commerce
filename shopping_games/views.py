from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import get_object_or_404

from .models import Game

def index(req):
  games = Game.objects.all()

  return render(req, "index.html", {"games": games})

def getById(req, id):
  game_found = Game.objects.get(id=id)

  game = [
    {
      "title": game_found.title,
      "description": game_found.description,
      "category": game_found.category,
      "img": game_found.img,
      "price": game_found.price,
      "available": game_found.available,
    }
  ]

  return render(req, "index.html", {"games": game})
