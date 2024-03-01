from django.db import models
from django.utils import timezone

class Game(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  category = models.CharField(max_length=50)
  img = models.ImageField(upload_to='apps/shopping_games/static/imgs')
  price = models.DecimalField(decimal_places=2, max_digits=10)
  units = models.IntegerField()
  rating = models.DecimalField(decimal_places=2, max_digits=10)
  available = models.BooleanField()
  created_at = models.DateTimeField(default=timezone.now())

  def __str__(self):
    return self.title