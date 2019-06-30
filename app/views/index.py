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
    (context, idioma, opcion, pagina) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, idioma, secciones)
    # texto foto
    texto_foto(pagina, idioma, secciones)
    # foto
    foto(view_name, idioma, secciones)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context.update(clase='inicio', secciones=secciones)
    response = render(request, 'app/pagina.html', context)
    return response
