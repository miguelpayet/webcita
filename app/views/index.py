from django.shortcuts import render

from app.common import carrusel
from app.common import foto
from app.common import texto_foto
from app.common import utils


def index(request):
    # logger
    # logger = logging.getLogger(__name__)
    # variables
    view_name = 'Inicio'
    (arr_idioma, arr_opcion, contact, cur_language, idioma, opcion, pagina, params) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, cur_language, secciones)
    # texto foto
    texto_foto(pagina, cur_language, secciones)
    # foto
    foto(view_name, cur_language, secciones)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context = {'clase': 'inicio', 'contacto': contact, 'cur_language': cur_language, 'idiomas': arr_idioma, 'opciones': arr_opcion,
               'params': params, 'secciones': secciones}
    response = render(request, 'app/pagina.html', context)
    return response
