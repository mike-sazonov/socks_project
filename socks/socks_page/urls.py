from django.urls import path
from . import views

urlpatterns = [
    path('socks/', views.SocksView.as_view(), name='socks'),
    path('socks/<int:pk>', views.SockDetail.as_view(), name='detail'),
    path('', views.StartPage.as_view(), name='start'),
]
