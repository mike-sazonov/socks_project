from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('my_page/', views.UserPage.as_view(), name='my_page'),
]
