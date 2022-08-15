from django.http import HttpResponse
from django.shortcuts import render
from .models import Novedades, Representantes, Sliders, Videos, Propiedades


def InicioView(request): #Pagina inicial
    slider = Sliders.objects.all()
    video = Videos.objects.all()
    context = {
        "slider": slider,
        "video": video,
    }
    return render(request, 'inicio.html', context)

def EmpresaView(request): #Pagina con la historia de la Empresa, por el momento se hardcodea
    return render(request, 'empresa.html', {})

def PropiedadesView(request): #Pagina con las propiedades de los moldes
    propiedad = Propiedades.objects.all()
    context = {
        "propiedad": propiedad
    }
    return render(request, 'propiedades.html', context)

def ServicioView(request): #Pagina de Servicio, por el momento se hardcodea
    return render(request, 'servicio.html', {})

def CatalogoView(request): #Pagina con el catalogo de los moldes
    return render(request, 'catalogo.html', {})

def RepresentantesView(request): #Pagina de Representantes
    representante = Representantes.objects.all()
    context = {
        "representante": representante
    }
    return render(request, 'representantes.html', context)

def NovedadesView(request): #Pagina de Novedades
    novedades = Novedades.objects.all()
    context = {
        'novedad': novedades
    }
    return render(request, 'novedades.html', context)

def ContactoView(request): #Pagina de Contacto
    return render(request, 'contacto.html', {})
