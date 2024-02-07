from django.shortcuts import render

# Create your views here.


def start_page(request):
    return render(request, 'socks_page/base.html')
