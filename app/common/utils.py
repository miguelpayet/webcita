from operator import itemgetter

from django.utils import translation

from app.common.opciones import opcion_actual
from app.common.opciones import opciones
from deprecated.secciones import contacto
from deprecated.secciones import idiomas
from deprecated.secciones import parametros
from app.models.Pagina import TextoPagina


def datos_comunes(view_name):
    # parametros
    cur_language = get_language()
    # idioma actual + lista de idiomas
    (idioma, arr_idioma) = idiomas(cur_language)
    # parametros
    params = parametros(idioma)
    # opciones y opción actual
    arr_opcion = opciones(view_name, idioma)
    opcion = opcion_actual(view_name)
    # datos de contacto
    contact = contacto(idioma)
    # pagina
    (pagina, dict_pagina) = get_pagina(opcion, idioma)
    # diccionario de contexto
    context = {'cur_language': idioma.codigo, 'contacto': contact, 'idiomas': arr_idioma, 'opciones': arr_opcion,
               'pagina': dict_pagina, 'params': params}
    return context, idioma, opcion, pagina


def get_language():
    return translation.get_language()


def get_pagina(opcion, idioma):
    try:
        pagina = opcion.pagina
    except Exception:
        raise Exception('opción %s no tiene página' % opcion.nombre)
    try:
        txt = pagina.textos.get(idioma=idioma)
    except TextoPagina.DoesNotExist:
        raise Exception("pagina %s no tiene textos en %s" % (pagina.nombre, idioma.nombre))
    return pagina, {'titulo_pagina': txt.titulo, 'descripcion_pagina': txt.descripcion}


# sortear las secciones por posicion
def sort_secciones(secciones):
    return sorted(secciones, key=itemgetter('posicion'))
