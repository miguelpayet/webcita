from django.shortcuts import render

from app.common import carrusel
from app.common import utils
from app.common.secciones import texto_foto


def tours(request):
    # variables
    view_name = 'Tours'
    (context, idioma, opcion, pagina) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, idioma, secciones)
    # seccion texto
    texto_foto(pagina, idioma, secciones)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context.update(clase='tours', secciones=secciones)
    response = render(request, 'app/pagina.html', context)
    return response
