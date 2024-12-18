from django.contrib import admin

from socks_page.admin import FavoritesInLine
from .models import User

# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['email', 'username']
    inlines = [FavoritesInLine]