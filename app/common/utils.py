from operator import itemgetter

from django.utils import translation

from app.common import contacto
from app.common import idiomas
from app.common import opciones
from app.common import parametros


def datos_comunes(view_name):
    # parametros
    cur_language = get_language()
    # parametros
    params = parametros(cur_language)
    # idioma actual + lista de idiomas
    (idioma, arr_idioma) = idiomas(cur_language)
    # opciones - le paso el nombre de la vista, me devuelve un tuple con las opciones y la opción actual
    (opcion, arr_opcion) = opciones(view_name, cur_language)
    # datos de contacto
    contact = contacto(cur_language)
    return arr_idioma, arr_opcion, contact, cur_language, idioma, opcion, params


def get_language():
    return translation.get_language()


# sortear las secciones por posicion
def sort_secciones(secciones):
    return sorted(secciones, key=itemgetter('posicion'))
