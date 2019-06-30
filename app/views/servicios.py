from django.shortcuts import render

from app.common import carrusel
from app.common import utils
from app.common.seccion_foto import foto
from app.common.secciones import texto


def servicios(request):
    # variables
    view_name = 'Servicios'
    (context, idioma, opcion, pagina) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, idioma, secciones)
    # seccion texto
    texto(pagina, idioma, secciones)
    # seccion foto
    foto(view_name, idioma, secciones)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context.update(clase='servicios', secciones=secciones)
    response = render(request, 'app/pagina.html', context)
    return response
