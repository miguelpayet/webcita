from operator import itemgetter

from django.db.models import Q
from django.utils import translation

from app.common.opciones import opcion_actual
from app.common.opciones import opciones
from app.models.Pagina import Pagina
from app.models.Pagina import TextoPagina
from deprecated.secciones import contacto
from deprecated.secciones import idiomas
from deprecated.secciones import parametros


def datos_comunes(view_name):
    # parametros
    cur_language = get_language()
    # idioma actual + lista de idiomas
    (idioma, arr_idioma) = idiomas(cur_language)
    # parametros
    params = parametros(idioma)
    # opciones y opción actual
    arr_opcion = opciones(idioma, view_name)
    # datos de contacto
    contact = contacto(idioma)
    # pagina
    opcion = opcion_actual(view_name)
    (pagina, dict_pagina) = get_pagina(opcion, idioma)
    # diccionario de contexto
    context = {'cur_language': idioma.codigo, 'contacto': contact, 'idiomas': arr_idioma, 'opcion_actual': opcion.nombre,
               'opciones': arr_opcion, 'pagina': dict_pagina, 'params': params}
    return context, idioma, pagina


def get_language():
    return translation.get_language()


def get_pagina(view_name, idioma):
    try:
        pagina = Pagina.objects.get(Q(opcion__nombre=view_name) | Q(subopcion__nombre=view_name))
    except Pagina.DoesNotExist:
        raise Exception('opción %s no tiene página' % view_name)
    try:
        txt = pagina.textos.get(idioma=idioma)
    except TextoPagina.DoesNotExist:
        raise Exception("pagina %s no tiene textos en %s" % (pagina.nombre, idioma.nombre))
    return pagina, {'descripcion': txt.descripcion, 'titulo': txt.titulo}


# sortear las secciones por posicion
def sort_secciones(secciones):
    return sorted(secciones, key=itemgetter('posicion'))
