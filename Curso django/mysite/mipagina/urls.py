from django.urls import path
from django.views.generic.base import View

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hora/', views.hora, name='hora'),
    path('temas/', views.bienvenida, name='bienvenida'),
    path('barras/', views.barras, name='barras'),
    path('video/', views.video_youtube, name='video'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('resultado/', views.resultado, name='resultado'),
    path('registro/', views.RegistroUsuario.as_view(), name="sing up"),
    path('saludo/', views.GreetingView.as_view(), name="saludo")
]