from django.contrib import admin
from .models import Socks

# Register your models here.


@admin.register(Socks)
class AdminSocks(admin.ModelAdmin):
    list_display = ['article', 'season', 'price']
