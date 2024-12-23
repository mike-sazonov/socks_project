from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model

from socks_page.models import Socks, Favorites
from .forms import UserForm

User = get_user_model()

# Create your views here.
class UserRegister(CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('start')

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            form.save()
            return super().form_valid(form)
        return render(self.request, 'accounts/register.html', self.get_context_data())

class UserPage(ListView):
    model = Socks
    template_name = 'accounts/user_page.html'
    context_object_name = 'socks'

    def get_queryset(self):
        return Socks.objects.filter(id__in=[i.sock_id for i in Favorites.objects.filter(user=self.request.user.id)])
