from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("shopping_games.urls")),
    path('admin/', admin.site.urls),
]
