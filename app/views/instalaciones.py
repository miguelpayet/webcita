from django.shortcuts import render

from app.common import carrusel
from app.common import instalacion
from app.common import utils


def instalaciones_cuartos(request):
    return instalaciones(request, 'Cuartos')


def instalaciones_ambientes(request):
    return instalaciones(request, 'Ambientes')


def instalaciones(request, view_name):
    # variables
    (context, idioma, opcion, pagina) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, idioma, secciones)
    # instalación
    instalacion(view_name, idioma, secciones)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context.update(clase='instalaciones', secciones=secciones)
    response = render(request, 'app/pagina.html', context)
    return response
