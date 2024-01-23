from django.shortcuts import render

from .models import Game

def index(req):
  games = Game.objects.all()

  return render(req, "index.html", {"games": games})
