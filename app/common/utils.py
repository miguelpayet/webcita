from operator import itemgetter

from django.utils import translation

from app.common.opciones import opcion_actual
from app.common.opciones import opciones
from app.common.secciones import contacto
from app.common.secciones import idiomas
from app.common.secciones import parametros


def datos_comunes(view_name):
    # parametros
    cur_language = get_language()
    # parametros
    params = parametros(cur_language)
    # idioma actual + lista de idiomas
    (idioma, arr_idioma) = idiomas(cur_language)
    # opciones y opción actual
    arr_opcion = opciones(view_name, cur_language)
    opcion = opcion_actual(view_name)
    # datos de contacto
    contact = contacto(cur_language)
    # pagina
    pagina = get_pagina(opcion)
    return arr_idioma, arr_opcion, contact, cur_language, idioma, opcion, pagina, params


def get_language():
    return translation.get_language()


def get_pagina(opcion):
    try:
        pagina = opcion.pagina
    except Exception:
        raise Exception('opción %s no tiene página' % opcion.nombre)
    return pagina


# sortear las secciones por posicion
def sort_secciones(secciones):
    return sorted(secciones, key=itemgetter('posicion'))
