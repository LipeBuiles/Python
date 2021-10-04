from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.views import View
from django.shortcuts import render


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