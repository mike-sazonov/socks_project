from django.shortcuts import render
from .models import Socks

# Create your views here.


def start_page(request):
    return render(request, 'socks_page/new.html')


def socks(request):
    socks = Socks.objects.all()
    return render(request, 'socks_page/socks.html', {'socks': socks})
