from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_HELLO),
    path('', views.say_hello),
    ]