from django.shortcuts import render
from .models import Socks
from django.views.generic.base import TemplateView
from django.views.generic import View, ListView
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
        return context


class SocksView(View):
    def get(self, request):
        form = SocksForm(request.GET)

        if form.is_valid():
            if form.changed_data:
                socks = Socks.objects.filter(
                    season__in=[
                        ('Лето', 'Зима')[form.cleaned_data['winter']],
                        ('Зима', 'Лето')[form.cleaned_data['summer']]],
                    gender__in=[form.cleaned_data['gender']]
                    )
            else:
                socks = Socks.objects.all()

        return render(request, 'socks_page/socks.html', {
            'forms': form,
            'socks': socks
        })
