from django.urls import path

from . import views

urlpatterns = [
    path('socks/', views.SocksView.as_view(), name='socks'),
    path('socks/<int:pk>', views.SockDetail.as_view(), name='detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('favorite/<int:pk>', views.FavoriteView.as_view(), name='favorite'), #?
    path('', views.StartPage.as_view(), name='start'),
]
