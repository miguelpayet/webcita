from operator import itemgetter

from django.shortcuts import render

from app.common import utils
from app.common.seccion_carrusel import carrusel
from app.common.seccion_foto import foto
from app.common.secciones import texto_foto


def index(request):
    # logger
    # logger = logging.getLogger(__name__)
    # variables
    view_name = 'Inicio'
    (arr_idioma, arr_opcion, contact, cur_language, idioma, opcion, params) = utils.datos_comunes(view_name)
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
    context = {'clase': 'inicio', 'contacto': contact, 'cur_language': cur_language, 'idiomas': arr_idioma, 'opciones': arr_opcion,
               'params': params, 'secciones': secciones}
    response = render(request, 'app/pagina.html', context)
    return response
