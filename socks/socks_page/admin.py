from django.contrib import admin
from .models import Socks, ImageSocks, MenuImage

# Register your models here.


@admin.register(Socks)
class AdminSocks(admin.ModelAdmin):
    list_display = ['article', 'season', 'price']


@admin.register(ImageSocks)
class AdminImageSocks(admin.ModelAdmin):
    list_display = ['image']

@admin.register(MenuImage)
class AdminMenuImage(admin.ModelAdmin):
    list_display = ['image']
