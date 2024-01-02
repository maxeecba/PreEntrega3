from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context
# Create your views here.


def hora(request):
    hora_actual= datetime.now().strftime(r"%d/%m/%Y - %H:%M:%S")
    nombre= "Maxi"
    ruta = open ("C:/Users/Look/Desktop/programando/PreEntrega3/PreEntrega3/core/templates/core/index.html")
    plantilla= Template(ruta.read())
    ruta.close()
    contexto = Context({"hora":hora_actual,"nombre":nombre})
    documento= plantilla.render(contexto)
    return HttpResponse(documento)

def saludo2(request):
    saludo= "hola"
    archivo= open("C:/Users/Look/Desktop/programando/PreEntrega3/PreEntrega3/core/templates/core/index2.html")
    leer_archivo= archivo.read()
    plantilla2= Template(leer_archivo)
    archivo.close()
    context = Context({"saludo2":saludo,})
    doc = plantilla2.render(context)
    return HttpResponse(doc)
class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

def edad_actual(request,fnac):
    
    fecha_actual= int(datetime.now().strftime(r"%Y"))
    calcular_años= fecha_actual - fnac
    persona1= Persona("juan",calcular_años)
    archivo = open ("C:/Users/Look/Desktop/programando/PreEntrega3/PreEntrega3/core/templates/core/index3.html")
    leer_archivo= archivo.read()
    plantilla = Template(leer_archivo)
    archivo.close()
    contexto = Context({"mi_edad": calcular_años, "anio_actual":fecha_actual,"nacimiento":fnac,"nombre":persona1.nombre,"edad":persona1.edad})
    Lo_que_retornamos  = plantilla.render(contexto)
    return HttpResponse(Lo_que_retornamos)