from django.urls import path
from . import views

utlpatterns = [
    path("", views.index, name="index"),
    path("boat", views.boat, name="boat"),
    path("bob", views.bob, name="bob"),
    path("flappydino", views.flappydino, name="flappydino"),
    path("foro", views.foro, name="foro"),
    path("IniciarSesion", views.IniciarSesion, name="IniciarSesion"),
    path("miner", views.miner, name="miner"),
    path("mydreamy", views.mydreamy, name="mydreamy"),
    path("pacman", views.pacman, name="pacman"),
    path("pinpong", views.pinpong, name="pinpong"),
    path("pokedex", views.pokedex, name="pokedex"),
    path("registrar", views.registrar, name="registrar"),
    path("tazita", views.tazita, name="tazita"),
    path("tetris", views.tetris, name="tetris")
]