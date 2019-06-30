from django.shortcuts import render

from app.common import carrusel
from app.common import utils
from app.common.secciones import texto


def quienes_somos(request):
    # variables
    view_name = 'Quienes Somos'
    (context, idioma, opcion, pagina) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, idioma, secciones)
    # seccion texto
    texto(pagina, idioma, secciones)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context.update(clase='quienes-somos', secciones=secciones)
    response = render(request, 'app/pagina.html', context)
    return response
