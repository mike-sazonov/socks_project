from django.contrib import admin
from .models import Socks, ImageSocks, MenuImage, Favorites

# Register your models here.
class FavoritesInLine(admin.TabularInline):
    model = Favorites
    extra = 1

@admin.register(Socks)
class AdminSocks(admin.ModelAdmin):
    list_display = ['article', 'season', 'price']
    inlines = [FavoritesInLine]


@admin.register(ImageSocks)
class AdminImageSocks(admin.ModelAdmin):
    list_display = ['image', 'product']
    list_filter = ['product']


@admin.register(MenuImage)
class AdminMenuImage(admin.ModelAdmin):
    list_display = ['image']