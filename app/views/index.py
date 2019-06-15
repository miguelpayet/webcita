from operator import itemgetter

from django.shortcuts import render
from django.utils import translation

from app.common.seccion_carrusel import carrusel
from app.common.seccion_foto import foto
from app.common.secciones import contacto
from app.common.secciones import idiomas
from app.common.secciones import opciones
from app.common.secciones import parametros
from app.common.secciones import texto_foto


def index(request):
    # logger
    # logger = logging.getLogger(__name__)
    # variables
    view_name = 'Inicio'
    cur_language = translation.get_language()
    # parametros
    params = parametros(cur_language)
    # idioma actual + lista de idiomas
    (idioma, arr_idioma) = idiomas(cur_language)
    # opciones - le paso el nombre de la vista, me devuelve un tuple con las opciones y la opción actual
    (opcion, arr_opcion) = opciones(view_name, cur_language)
    # datos de contacto
    contact = contacto(cur_language)
    # secciones
    secciones = []
    # carrusel
    carrusel(opcion, cur_language, secciones)
    # texto foto
    texto_foto(opcion, cur_language, secciones)
    # foto
    arr_foto = foto(view_name, cur_language)
    secciones.append(arr_foto)
    # sortear las secciones por posicion
    secciones = sorted(secciones, key=itemgetter('posicion'))
    # invocar vista
    context = {'contacto': contact, 'cur_language': cur_language, 'idiomas': arr_idioma, 'opciones': arr_opcion, 'params': params,
               'secciones': secciones}
    response = render(request, 'app/index.html', context)
    return response
