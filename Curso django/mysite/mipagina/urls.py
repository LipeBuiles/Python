from django.urls import path
from django.views.generic.base import View

from . import views

urlpatterns = [
    path('inicio', views.index, name='index'),
    path('hora/', views.hora, name='hora'),
    path('temas/', views.bienvenida, name='bienvenida'),
    path('barras/', views.barras, name='barras'),
    path('video/', views.video_youtube, name='video')
]