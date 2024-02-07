from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Socks(models.Model):
    W = 'W'
    S = 'S'
    SEASON = [
        (W, 'Winter'),
        (S, 'Summer')
    ]
    article = models.CharField(max_length=50)
    season = models.CharField(max_length=1, choices=SEASON, default=S)
    price = models.IntegerField(validators=[MinValueValidator(1)])


