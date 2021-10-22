from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.views import View
from django.shortcuts import render
from mipagina.models import Personas
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.template.loader import get_template
from .forms import*
from django.urls import reverse_lazy
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("Hola mundo")

def hora(request):
    hora_actual = datetime.now()
    documento_plantilla = open(r"mipagina\templates\plantilla1.html")
    plantilla = Template(documento_plantilla.read())
    documento_plantilla.close()
    contexto = Context({"hora": hora_actual})
    documento_final = plantilla.render(contexto)

    return HttpResponse(documento_final)



class GreetingView(View):
    greeting = "OK"
    def get(self, request):
        return HttpResponse(self.greeting)

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def bienvenida(request):
    persona_1 = Persona("Juan", "Builes")
    temas_del_curso = ["Plantillas", "Modelos", "Bases de Datos", "Vistas"]
    contexto = {"nombre": persona_1.nombre,
                "apellido": persona_1.apellido,
                "temas": temas_del_curso}

    return render(request, "plantilla2.html", contexto)

def barras(request):
    return render(request, "vista2.html")

def video_youtube(request):
    return render(request, "video.html")

def busqueda(request):
    return render(request, "busqueda.html")

def resultado(request):
    if request.GET["prd"]:
        persona = request.GET["prd"]
        if len(persona)>20:
            mensaje = "Texto de busqueda demasiado largo"
        else:
            estudiantes = Personas.objects.filter(nombre = persona)
            return render(request, "resultado.html", {"estudiantes": estudiantes,  "query": persona})
    else:
        
        mensaje = "No has introducido  nada"
    return HttpResponse(mensaje)

class RegistroUsuario(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("saludo")
    template_name = "registro.html"

class ListUsuarios(ListView):
    model = User
    template_name = "lista.html"

class EliminarUsuario(DeleteView):
    model = User
    success_url = reverse_lazy("saludo")
    template_name = "Eliminar.html"
