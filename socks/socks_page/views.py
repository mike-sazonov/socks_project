from django.shortcuts import render
from .models import Socks
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.
menu = {
    '/socks': 'Каталог продукции',
    '/about': 'О нас',
    '/delivery': 'Доставка',
    '/Contacts': 'Контакты'
}


class StartPage(TemplateView):
    template_name = 'socks_page/start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class SocksView(ListView):
    template_name = 'socks_page/socks.html'
    model = Socks
    context_object_name = 'socks'