from django.urls import path
from . import views

urlpatterns = [
    path('socks/', views.socks, name='socks'),
    path('', views.start_page),
]
