from django.shortcuts import render

from app.common import carrusel
from app.common import utils
from app.common.secciones import texto_foto


def tours(request):
    # variables
    view_name = 'Tours'
    (arr_idioma, arr_opcion, contact, cur_language, idioma, opcion, pagina, params) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, cur_language, secciones)
    # seccion texto
    texto_foto(pagina, cur_language, secciones)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context = {'clase': 'tours', 'contacto': contact, 'cur_language': cur_language, 'idiomas': arr_idioma, 'opciones': arr_opcion,
               'params': params, 'secciones': secciones}
    response = render(request, 'app/pagina.html', context)
    return response
