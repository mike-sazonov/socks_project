from django.shortcuts import render
from .models import Socks
from django.views import View

# Create your views here.


class StartPage(View):
    def get(self, request):
        return render(request, 'socks_page/new.html')


class SocksView(View):
    def get(self, request):
        socks = Socks.objects.all()
        return render(request, 'socks_page/socks.html', {'socks': socks})