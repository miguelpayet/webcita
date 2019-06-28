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
    (arr_idioma, arr_opcion, contact, cur_language, idioma, opcion, pagina, params) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, cur_language, secciones)
    # instalación
    instalacion(view_name, cur_language, secciones)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context = {'clase': 'instalaciones', 'contacto': contact, 'cur_language': cur_language, 'idiomas': arr_idioma, 'opciones': arr_opcion,
               'params': params, 'secciones': secciones}
    response = render(request, 'app/pagina.html', context)
    return response
