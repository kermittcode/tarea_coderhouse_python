from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader

# Create your views here.

def Familiares(self):

    mi_html = open('C:/Users/natar/Desktop/Tarea_Coder_Python/MVT Ibañez/ProyectoTarea/plantillas/template1.html')

    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto = Context(Familiares)

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)