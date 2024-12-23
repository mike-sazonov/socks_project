from django.urls import path
from . import views
from .decorators import check_recaptcha

urlpatterns = [
    path('register/', check_recaptcha(views.UserRegister.as_view()), name='register'),
    path('my_page/', views.UserPage.as_view(), name='my_page'),
]
