from django.shortcuts import render
from .models import Socks, MenuImage
from django.views.generic.base import TemplateView
from django.views.generic import View, DetailView
from .forms import SocksForm


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
        context['images'] = MenuImage.objects.all()
        return context


class SocksView(View):
    def get(self, request):
        form = SocksForm(request.GET)

        if form.is_valid():
            if form.changed_data:    # если фильтры не пустые
                socks = Socks.objects.filter(
                    season__in=[
                        ('Лето', 'Зима')[form.cleaned_data['winter']],
                        ('Зима', 'Лето')[form.cleaned_data['summer']]],
                    gender__in=form.cleaned_data['gender'].split(' ')
                    )
            else:
                socks = Socks.objects.all()

        return render(request, 'socks_page/socks.html', {
            'forms': form,
            'socks': socks
        })


class SockDetail(DetailView):
    model = Socks
    template_name = 'socks_page/sock_detail.html'
    context_object_name = 'sock'
