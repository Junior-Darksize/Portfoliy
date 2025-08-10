from django.urls import path
from .views import home,service

urlpatterns = [
    path("home/",home,name='home'),
    path("service/",service,name='service')
]