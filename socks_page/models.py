from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

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
    UNISEX = 'Унисекс'
    CHILD = 'Детский'

    GENDER = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
        ('Унисекс', 'Унисекс'),
        ('Детский', 'Детский')
    ]
    article = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default='Носки')
    season = models.CharField(max_length=4, choices=SEASON, default=SMMR)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    gender = models.CharField(max_length=7, choices=GENDER, default=WOMEN)
    start_image = models.FileField(upload_to='start_images', null=True)
    description = models.TextField(default="не указано")
    fabric = models.TextField(default="состав не указан")
    user = models.ManyToManyField(User, null=True)

    def __str__(self):
        return f'{self.article} {self.gender} {self.price}'


class ImageSocks(models.Model):
    product = models.ForeignKey(Socks, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to='socks_gallery')


class MenuImage(models.Model):
    image = models.FileField(upload_to='menu_field')


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sock = models.ForeignKey(Socks, on_delete=models.CASCADE)
