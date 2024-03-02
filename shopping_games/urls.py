from django.urls import path
from .views import index, getById

urlpatterns = [
  path("", index),
  path("<int:id>", getById),
]
