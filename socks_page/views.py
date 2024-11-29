from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic.edit import FormMixin

from .models import Socks, MenuImage
from django.views.generic.base import TemplateView
from django.views.generic import View, DetailView, ListView, FormView
from django.core.files.images import get_image_dimensions
from .forms import SocksForm


def r_div(x):   # функция для определения соотношения сторон изображения
    return round(x[0] / x[1])

# Create your views here.
menu = {
    '/socks': 'Каталог продукции',
    '/about': 'О нас',
    '/delivery': 'Доставка',
    '/contacts': 'Контакты'
}


class StartPage(TemplateView):
    template_name = 'socks_page/start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['images_lg'] = [img for img in MenuImage.objects.all() if r_div(get_image_dimensions(img.image)) == 3]
        context['images_sm'] = [img for img in MenuImage.objects.all() if r_div(get_image_dimensions(img.image)) != 3]
        return context

class SocksView(ListView):
    model = Socks
    template_name = 'socks_page/socks.html'
    context_object_name = 'socks'
    form_class = SocksForm
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['forms'] = self.form_class(self.request.GET)
        return context

    def get_queryset(self):
        form = self.form_class(self.request.GET)

        if form.is_valid():
            if form.changed_data:    # если фильтры не пустые
                return Socks.objects.filter(
                    season__in=[
                        ('Лето', 'Зима')[form.cleaned_data['winter']],
                        ('Зима', 'Лето')[form.cleaned_data['summer']]],
                    gender__in=form.cleaned_data['gender'].split(' ')
                    )
            else:
                return Socks.objects.all()


class SockDetail(DetailView):
    model = Socks
    template_name = 'socks_page/sock_detail.html'
    context_object_name = 'sock'


class AboutView(TemplateView):
    template_name = 'socks_page/about.html'


class DeliveryView(TemplateView):
    template_name = 'socks_page/delivery.html'


class ContactsView(TemplateView):
    template_name = 'socks_page/contacts.html'
