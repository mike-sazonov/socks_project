from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Socks(models.Model):
    WNTR = 'Зима'
    SMMR = 'Лето'
    SEASON = [
        ('Зима', 'Зима'),
        ('Лето', 'Лето')
    ]
    MEN = 'Мужской'
    WOMEN = 'Женский'
    СHILD = 'Детский'

    GENDER = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
        ('Детский', 'Детский')
    ]
    article = models.CharField(max_length=50)
    season = models.CharField(max_length=4, choices=SEASON, default=SMMR)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    gender = models.CharField(max_length=7, choices=GENDER, default=WOMEN)
    start_image = models.FileField(upload_to='start_images', null=True)

    def __str__(self):
        return f'{self.article} {self.gender} {self.price}'


class ImageSocks(models.Model):
    product = models.ForeignKey(Socks, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to='socks_gallery')
